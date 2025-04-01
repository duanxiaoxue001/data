import os
import pickle
import matplotlib.pyplot as plt
#
save_directory = ("D:\Reinforcement learning\IPPSQL - punish\schedules\\results.8-2-1")
best_schedule = None
best_time = float('inf')
best_reward = None
for subfolder in os.listdir(save_directory):
    filepath = os.path.join(save_directory, subfolder)
    with open(filepath, 'rb') as f:
        data = pickle.load(f)
        schedule = data["schedule"]
        total_time = data["total_time"]
        # print(total_time)
        total_reward = data["total_reward"]
        # print(schedule)
        # print(total_reward)
        subfolder = subfolder
        # print(n)

        if total_time < best_time:
            best_time = total_time
            best_schedule = schedule
            best_reward = total_reward
            best_filename = subfolder
print("次数:", best_filename)
print("最佳调度序列:", best_schedule)
print("最佳时间:", best_time)
print("总奖励:", best_reward)
