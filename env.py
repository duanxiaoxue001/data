import gym
from gym import spaces
import numpy as np
import random
import pickle
import os
INF = float('inf')

file_path = r"D:\Reinforcement learning\IPPSQL.1\process"

class FlexibleFlowShopEnv(gym.Env):
    def __init__(self, num_machines, num_operations, computation_time_matrix1, communication_time_matrix1, in_OR1):
        super(FlexibleFlowShopEnv, self).__init__()
        self.num_machines = num_machines
        self.num_operations = num_operations
        self.processing_times = computation_time_matrix1
        self.in_OR1 = in_OR1
        self.threshold = float("inf")
        self.iteration = 0  # 在这里初始化 self.iteration
        # 设置通信时间矩阵
        self.communication_time_matrix = np.copy(communication_time_matrix1)
        self.initial_communication_time_matrix = np.copy(communication_time_matrix1)
        self.original_communication_time_matrix = np.copy(communication_time_matrix1)

        # 状态空间: 9
        self.observation_space = spaces.Discrete(num_operations)

        # 动作空间: 操作编号（1到num_operations）和机器编号（1到num_machines）
        self.action_space = spaces.MultiDiscrete([num_operations + 1, num_machines + 1])

        self.original_ready_operations = []  # 添加原始就绪操作属性

        self.reset()

    def reset(self):
        self.schedule = []
        self.current_operation = 0
        self.machine_end_times = [0] * self.num_machines  # 初始化每台机器的结束时间
        self.operation_end_times = [0] * self.num_operations  # 初始化每个操作的结束时间
        self.machine_available_times = [0] * self.num_machines  # 初始化每台机器的可用时间
        self.operation_times = {}  # 记录每个操作的开始和结束时间
        self.communication_time_matrix = np.copy(self.initial_communication_time_matrix)
        communication_time_matrix1_T = np.transpose(self.communication_time_matrix)
        self.ready_operations = [i + 1 for i, column in enumerate(communication_time_matrix1_T) if
                                 all(column[j] == INF for j in range(len(column)) if j != i)]

        self.original_ready_operations = self.ready_operations.copy()  # 保存原始就绪操作
        print(f"初始就绪操作: {self.ready_operations}")
        return self.get_observation()

    def step(self, action):
        operation, machine = action
        machine_index = machine - 1
        operation_index = operation - 1
        # print(operation_index, machine, operation, machine)
        computation_time = self.processing_times[operation_index][machine]

        prev_operations = [i + 1 for i, row in enumerate(self.original_communication_time_matrix)
                if row[operation_index] == 0]
        # 过滤出已经执行过的前置操作
        executed_prev_operations = [op for op in prev_operations if self.operation_end_times[op - 1] > 0]
        if executed_prev_operations:
           # 如果存在已执行的前置操作，选择它们中结束时间的最大值
            prev_operation_end_time = max(self.operation_end_times[op - 1] for op in executed_prev_operations)
        else:
        # 如果没有已执行的前置操作，则使用机器的结束时间
            prev_operation_end_time = self.machine_end_times[machine_index]
        # 计算此操作在所选机器上的开始时间：应该是机器当前结束时间和已执行前置操作结束时间中的最大值
        start_time = max(self.machine_end_times[machine_index], prev_operation_end_time)
        end_time = start_time + computation_time

        # 更新机器和操作的结束时间
        self.machine_end_times[machine_index] = end_time
        self.operation_end_times[operation_index] = end_time
        self.machine_available_times[machine_index] = end_time

        # 记录操作的开始和结束时间
        self.operation_times[operation] = (start_time, end_time, machine)

        # 打印调度时间
        print(f"Operation {operation} scheduled on machine {machine} from {start_time} to {end_time}")
        file_path = r"D:\Reinforcement learning\IPPSQL - punish\process\schedule_times.8-2-1.txt"
        with open( file_path, "a") as f:
            f.write(f"Operation {operation} scheduled on machine {machine} from {start_time} to {end_time}\n")
        if operation not in self.ready_operations:
            raise ValueError(f"Invalid operation: {operation}. Must be one of {self.ready_operations}.")

        # 将动作加入调度序列
        self.schedule.append((operation, machine))

        # 从就绪操作列表中移除已执行的操作
        self.ready_operations.remove(operation)

        # 更新就绪操作列表,添加与当前操作相连的下一个操作
        self.update_ready_operations(operation)

        self.done = len(self.ready_operations) == 0

        reward = self.calculate_reward(operation, machine)
        observation = self.get_observation()
        if self.done:
            self.communication_time_matrix = np.copy(self.initial_communication_time_matrix)

        return observation, reward, self.done, {}

    def get_total_time(self):
        return max(self.machine_end_times)  # 返回所有机器结束时间中的最大值作为总时间

    def update_ready_operations(self, operation):
        next_operations = []
        for i in range(len(self.communication_time_matrix[operation - 1])):
            if self.communication_time_matrix[operation - 1][i] == 0:
                next_operations.append(i + 1)
                self.communication_time_matrix[operation - 1][i] = INF

        in_or_group = [op for op in next_operations if any(op in or_group for or_group in self.in_OR1)]

        if in_or_group:
            chosen_operations = []
            for or_group in self.in_OR1:
                group_ops = [op for op in in_or_group if op in or_group]
                if group_ops:
                    chosen_operations.append(np.random.choice(group_ops))
            # 添加不属于 OR 节点的操作到 chosen_operations 中
            non_or_ops = [op for op in next_operations if op not in in_or_group]
            chosen_operations.extend(non_or_ops)

            for op in chosen_operations:
                if all(self.machine_available_times[m - 1] >= 0 for m in self.processing_times[op - 1]):
                    if op not in self.ready_operations:
                        self.ready_operations.append(op)
        else:
            chosen_operations = next_operations
            for current_operation in chosen_operations:
                # 获取当前操作的所有前置操作
                predecessors = [j + 1 for j in range(len(self.communication_time_matrix))
                                if self.original_communication_time_matrix[j][current_operation - 1] != INF]

                # 检查前置操作中是否有属于 OR 节点的操作
                or_predecessors = [predecessor for predecessor in predecessors if
                                   any(predecessor in or_group for or_group in self.in_OR1)]
                non_or_predecessors = [predecessor for predecessor in predecessors if
                                       predecessor not in or_predecessors]

                # 只有在所有前置操作都已完成的情况下，才允许添加// 分为OR节点和非OR节点
                # 多条件判断
                if not non_or_predecessors:
                    # 只有 OR 节点的前置操作，任意一条完成
                    if any(predecessor in [op[0] for op in self.schedule] for predecessor in or_predecessors):
                        if all(self.machine_available_times[m - 1] >= 0 for m in
                               self.processing_times[current_operation - 1].keys()):
                            if current_operation not in self.ready_operations:
                                self.ready_operations.append(current_operation)
                elif not or_predecessors:
                    # 只有非 OR 节点的前置操作，所有需完成
                    if all(predecessor in [op[0] for op in self.schedule] for predecessor in non_or_predecessors):
                        if all(self.machine_available_times[m - 1] >= 0 for m in
                               self.processing_times[current_operation - 1].keys()):
                            if current_operation not in self.ready_operations:
                                self.ready_operations.append(current_operation)
                else:
                    # 同时有 OR 和非 OR 节点的前置操作，需满足两个条件
                    if (any(predecessor in [op[0] for op in self.schedule] for predecessor in or_predecessors) and
                            all(predecessor in [op[0] for op in self.schedule] for predecessor in non_or_predecessors)):
                        if all(self.machine_available_times[m - 1] >= 0 for m in
                               self.processing_times[current_operation - 1].keys()):
                            if current_operation not in self.ready_operations:
                                self.ready_operations.append(current_operation)

    def get_observation(self):
        observation = np.zeros(self.observation_space.n, dtype=int)
        for op in self.ready_operations:
            observation[op - 1] = 1
        return observation

    def calculate_reward(self, operation, machine):  # 奖励设置
        max_processing_time = max(self.processing_times[operation - 1].values())
        current_processing_time = self.processing_times[operation - 1].get(machine, INF)
        reward = max_processing_time - current_processing_time
        return reward

    def choose_action_randomly(self):
        operation = np.random.choice(self.ready_operations)
        possible_machines = [m for m in self.processing_times[operation - 1].keys() if
                             self.machine_available_times[m - 1] <=0]
        if not possible_machines:
            possible_machines = [m for m in self.processing_times[operation - 1].keys()]
        machine = np.random.choice(possible_machines)
        return operation, machine


# # 测试环境
# env = FlexibleFlowShopEnv(
#     num_machines=4,
#     num_operations=10,
#     # computation_time_matrix1=[
#     #         {1: 39.7, 2: 28.8},
#     #         {1: 40.6, 2: 53.8, 3: 12.3},
#     #         {2: 61.8, 3: 30.7},
#     #         {1: 18.3, 3: 17.1}
#     #      ],
#     computation_time_matrix1=[
#            {1: 39.7, 2: 28.8}, {1: 40.6, 2: 53.8, 3: 12.3}, {2: 61.8, 4: 30.7}, {1: 18.3, 3: 17.1, 4: 66.4},
#            {1: 40.1, 3: 79.5},
#            {1: 20.7, 2: 14.5, 3: 47.6, 4: 43.7}, {2: 62.4, 3: 14.9, 4: 54.1}, {1: 35.0, 2: 52.7, 4: 54.7},
#            {1: 19.2, 2: 26.8, 3: 32.7, 4: 69.8}, {3: 77.4, 4: 31.5}
#     ],
#     # communication_time_matrix1=[
#     #     [INF, 0, 0, INF],
#     #     [INF, INF, INF, 0],
#     #     [INF, INF, INF, 0],
#     #     [INF, INF, INF, INF]
#     # ],
#     communication_time_matrix1=[
#           [INF, 0, INF, 0, INF, INF, INF, INF, INF, INF],
#           [INF, INF, 0, INF, INF, INF, INF, INF, INF, INF],
#           [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
#           [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
#           [INF, INF, INF, INF, INF, 0, INF, INF, INF, INF],
#           [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
#           [INF, INF, INF, INF, INF, INF, INF, 0, 0, INF],
#           [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
#           [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
#           [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
#     ],
#     # in_OR1=[2, 3]
#     in_OR1=[2, 3, 4, 8, 9]
# )
# obs = env.reset()
# done = False
#
# while not done:
#     action = env.choose_action_randomly()  # 使用随机选择策略
#     obs, reward, done, info = env.step(action)
#     print(f"Action: {action}, Reward: {reward}, Done: {done}, Ready Operations: {env.ready_operations}")
#
# print("Final Schedule Sequence:", env.schedule)


