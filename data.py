INF = float('inf')
def final_matrix(a, b, c):
    computation_time_matrix=[]
    communication_time_matrix=[]
    in_OR = []

    computation_time_matrix = a

    print(computation_time_matrix)

    task_number=0  # 任务总数
    task_number_list = []   # 存储每个子列表中任务的累计数量
    for i in b:
        task_number += len(i)
        task_number_list.append(task_number)
    task_number_list1 = [0]+task_number_list

    for j in range(len(b)):
        for l in b[j]:
            temp=[]
            for p in range(task_number_list1[j]):
                temp.append(INF)
            temp+=l
            for q in range(task_number_list1[j+1],task_number):
                temp.append(INF)
            communication_time_matrix.append(temp)
    print(communication_time_matrix)


    for i, sublist in enumerate(c):
        for tup in sublist:
            tuple_sublist = tup
            v = task_number_list1[i]
            updated_tuple = tuple(elem + v if isinstance(elem, int) else elem for elem in tuple_sublist)
            in_OR.append(updated_tuple)
    print(in_OR)
    print("\n")
    return computation_time_matrix, communication_time_matrix, in_OR

# job = 0
# num_machines = 5
# num_operations = 16
# computation_time_matrix = [{1: 39.7, 2: 28.8, 3: 15.6}, {1: 40.6, 2: 53.8, 4: 12.3}, {2: 61.4, 4: 30.7}, {1: 18.3, 3: 17.1, 4: 66.4, 5: 25.7},
#                            {1: 40.1, 3: 79.5}, {1: 20.7, 2: 14.5, 3: 47.6, 4: 43.7}, {2: 62.4, 3: 14.9, 4: 54.7, 5: 32.1}, {1: 35.0, 2: 52.7, 4: 54.7},
#                            {1: 19.2, 2: 26.8, 3: 32.7, 4: 69.8, 5: 13.6}, {3: 77.4, 4: 31.5}, {2: 18.6, 4: 24.7, 5: 32.4}, {1: 51.2, 5: 16.8},
#                            {2: 31.2, 3: 51.2, 5: 24.6}, {1: 21.6, 2: 14.2, 3: 8.6, 4: 12.6, 5: 31.7}, {3: 16.7, 5: 41.2}, {1: 21.7, 4: 41.3, 5: 31.6}
#                         ]
# communication_time_matrix = [
#                 [INF, 0, INF, 0, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
#                 [INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
#                 [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
#                 [INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
#                 [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
#                 [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
#                 [INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
#                 [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
#                 [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, 0, INF, 0],
#                 [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, 0, INF, INF, INF, INF],
#                 [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF],
#                 [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF],
#                 [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
#                 [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF],
#                 [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
#                 [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
#     ]
# in_OR = [(2, 3, 4, 5, 6), (10, 14, 15, 16)]
# num_machines_max = 15
# num_operations_max = 15

""" job1 """
computation_time_matrix1 = [{3: 16.7, 6: 14.1, 8: 25.6}, {12: 20.8, 14: 18.9}, {4: 30.1, 5: 41.5, 7: 18.9},
                            {2: 21.5, 6: 12.6, 8: 40.1}, {9: 13.1}, {12: 7.9}, {4: 31.4, 6: 61.2},
                            {5: 9.1, 7: 13.5}],
communication_time_matrix1 = [
                               [INF, 0, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, 0, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, 0, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF]
                              ],
in_OR1 = [],

""" job2 """
computation_time_matrix2 = [{1: 16.2, 3: 18.4, 5: 27.3}, {5: 14.3, 7: 16.1}, {2: 41.3, 4: 36.2},
                            {10: 11.7, 11: 15.8, 12: 21.3}, {6: 31.2, 8: 25.4, 13: 31.6}, {3: 8.9, 5: 11.6}],
communication_time_matrix2 = [
                              [INF, 0, INF, 0, 0, INF],
                              [INF, INF, 0, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, 0],
                              [INF, INF, INF, INF, INF, INF]
                              ],
in_OR2 = [],

"""job3"""
computation_time_matrix3 = [{2: 21.3, 5: 35.6, 6: 17.8}, {3: 6.7, 7: 12.3, 9: 17.8}, {11: 36.7, 14: 41.2},
                            {13: 21.8, 14: 14.6, 15: 11.9}, {6: 14.5, 7: 16.7}, {8: 51.4, 9: 47.8, 12: 12.8},
                            {3: 6.8, 4: 13.6}, {1: 19.9, 5: 25.6, 9: 21.2, 14: 30.7}, {4: 26.7, 6: 45.5},
                            {8: 21.8, 9: 19.9, 14: 34.7}, {11: 26.3, 13: 18.1, 14: 31.4, 15: 16.2}, {1: 9.1, 6: 14.5, 8: 19.6},
                            {2: 16.8, 3: 24.5}, {3: 28.9, 6: 18.4, 9: 19.7, 11: 23.5}],
communication_time_matrix3 = [
                               [INF, 0, 0, INF, INF, 0, INF, 0, INF, INF, 0, 0, INF, 0],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                             ],
in_OR3 = [(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)],


""" job4 """
computation_time_matrix4 = [{5: 32.1}, {12: 15.3, 15: 18.9}, {1: 14.6, 6: 15.7, 9: 16.9},
                            {2: 21.4, 6: 18.8, 8: 12.4}, {1: 14.6, 12: 18.7, 14: 19.2}, {1: 8.9, 5: 14.7, 8: 16.7, 9: 12.3, 12: 19.5},
                            {3: 16.2, 6: 12.9, 8: 19.4}, {4: 24.6, 7: 28.9, 10: 15.1}, {4: 41.3, 8: 26.9},
                            {5: 50.7, 9: 44.6, 11: 51.1, 14: 29.9}],
communication_time_matrix4 = [
                              [INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, 0, 0, INF, 0, INF, 0, INF, 0],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, 0, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, 0, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
                              ],
in_OR4 = [(3, 4, 5, 6, 7, 8, 9, 10)]

"""job5"""
computation_time_matrix5 = [{2: 13.4, 9: 16.6}, {12: 21.4, 14: 36.7, 15: 51.2}, {3: 21.6, 5: 27.1, 7: 33.2},
                            {1: 5.9, 9: 16.2, 10: 18.9, 12: 20.3}, {4: 18.1, 5: 14.6}, {6: 23.4, 8: 31.2, 9: 16.8, 13: 14.7},
                            {3: 16.7, 6: 19.9, 8: 9.8}, {11: 21.3, 13: 15.1, 15: 31.7}, {2: 25.6, 6: 12.8, 10: 31.1},
                            {6: 17.9, 10: 19.2, 13: 21.6}, {1: 31.6, 9: 26.8}],
communication_time_matrix5 = [
                              [INF, 0, INF, INF, 0, 0, INF, 0, 0, 0, INF],
                              [INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              ],
in_OR5 = [(2, 3, 4, 5, 6, 7), (8, 9)],

""" job6 """
computation_time_matrix6 = [{12: 31.2, 14: 26.7, 15: 15.8}, {3: 6.8, 13: 14.5}, {2: 12.4, 8: 16.7, 12: 8.9, 14: 24.5},
                            {4: 16.7, 7: 13.2, 8: 26.5}, {1: 25.6, 5: 18.9, 9: 31.5}, {9: 19.9, 12: 11.1, 15: 22.3},
                            {6: 41.2, 13: 32.5}, {5: 16.3, 8: 17.1, 12: 26.2}, {10: 16.8, 13: 18.9, 15: 25.6},
                            {2: 21.4, 4: 19.1, 6: 30.4, 8: 17.6}],
communication_time_matrix6 = [[INF, 0, 0, INF, 0, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, 0, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, 0, INF, 0, INF],
                              [INF, INF, INF, INF, INF, INF, INF, 0, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              ],
in_OR6 = [(2, 3, 4, 5), (7, 8, 9, 10)],

""" job7 """
computation_time_matrix7 = [{4: 13.6, 7: 17.8}, {13: 20.1, 14: 18.9, 15: 19.9}, {3: 18.3, 6: 16.5, 7: 30.1, 8: 28.6},
                            {2: 8.9, 12: 15.6, 14: 11.4}, {1: 6.7, 9: 11.3, 11: 14.5, 15: 27.1}, {3: 34.5, 5: 41.2, 7: 21.7},
                            {1: 17.3, 9: 13.4, 10: 17.8, 11: 14.5}, {10: 23.5, 11: 26.7, 13: 19.8}, {4: 14.5, 6: 12.3, 7: 18.6},
                            {2: 24.5, 8: 18.9}, {1: 51.2, 7: 31.4, 12: 30.1, 15: 29.4}],
communication_time_matrix7 = [[INF, 0, INF, INF, 0, 0, INF, 0, INF, INF, 0],
                              [INF, INF, 0, 0, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, 0, 0, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
                              ],
in_OR7 = [(2, 5, 6, 7, 8, 11)],

""" job8 """
computation_time_matrix8 = [{5: 31.5, 13: 52.6}, {6: 36.7, 7: 37.8, 9: 31.9}, {1: 41.3, 3: 46.7, 8: 38.9},
                            {11: 16.7, 14: 18.9}, {2: 25.6, 6: 22.8, 8: 16.5}, {6: 37.8, 9: 40.1, 12: 35.6},
                            {12: 18.9, 14: 15.6}, {1: 31.6, 3: 37.8, 6: 40.3, 7: 29.6, 9: 26.8}, {12: 18.3, 13: 19.2},
                            {4: 26.7, 10: 21.9, 13: 30.7}]
communication_time_matrix8 = [[INF, 0, INF, INF, INF, 0, INF, 0, INF, INF],
                              [INF, INF, 0, 0, 0, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, 0, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
                              ]
in_OR8 = [(3, 4, 5)]

""" job9 """
computation_time_matrix9 = [{6: 32.6, 7: 27.8, 8: 24.3}, {1: 15.6, 4: 25.6, 6: 29.8, 9: 30.1}, {2: 31.2, 7: 36.7, 10: 38.9, 11: 40.2},
                            {5: 18.9, 7: 21.4, 13: 19.2, 14: 23.6}, {11: 13.4, 13: 16.7, 15: 20.1}, {6: 25.6, 7: 24.1, 8: 27.8, 9: 19.9},
                            {8: 15.6, 9: 6.7, 11: 18.3}, {6: 23.4, 7: 27.8, 8: 25.3, 9: 28.9}, {11: 21.4, 14: 28.3, 15: 23.7},
                            {12: 31.4, 13: 36.2}, {3: 26.7, 6: 28.9, 14: 30.1}, {2: 12.3, 7: 9.9, 9: 11.4},
                            {5: 25.6, 15: 24.3}],
communication_time_matrix9 = [[INF, 0, 0, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, 0, 0, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, 0],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                              ],
in_OR9 = [(2, 3, 4), (9, 10), (12, 13)],

""" job10 """
job10 = 10
computation_time_matrix10 = [{7: 7.9}, {12: 24.5, 14: 21.6, 15: 25.6}, {3: 21.4, 8: 26.7, 12: 29.1},
                             {5: 12.3, 7: 9.8, 9: 11.6, 11: 16.4}, {1: 31.3, 6: 35.6, 13: 38.9, 15: 40.5}, {2: 14.5, 4: 16.7, 8: 15.3, 10: 19.4},
                             {4: 25.6, 6: 21.3, 8: 27.8}, {11: 41.2, 12: 46.7, 13: 49.5, 14: 50.1, 15: 47.4}, {2: 25.6, 3: 21.3, 4: 27.8},
                             {5: 31.2, 10: 28.9, 14: 34.6}, {11: 21.3, 13: 19.4, 15: 18.9}, {2: 17.8, 6: 12.3},
                             {7: 25.6, 8: 17.8, 10: 26.7}, {2: 35.6, 14: 30.2, 15: 41.1}, {3: 14.5, 5: 17.8, 7: 23.6, 9: 25.6, 10: 19.3}],
communication_time_matrix10 = [[INF, 0, INF, INF, INF, 0, INF, 0, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
                               [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
                               [INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
                               ],
in_OR10 = [(2, 3, 4, 5, 6, 7, 8, 9, 10)],

""" job11 """
computation_time_matrix11 = [{8: 35.6, 10: 38.9, 12: 30.1}, {2: 26.7, 6: 31.2, 8: 28.9, 9: 19.8, 10: 21.4}, {13: 21.3, 14: 26.7, 15: 31.2},
                             {2: 15.6, 13: 19.8}, {1: 24.5, 6: 21.8, 15: 31.2}, {3: 17.8, 12: 23.4, 13: 25.3},
                             {5: 25.6, 9: 27.8, 10: 29.9, 12: 20.1}, {4: 17.9, 14: 14.5, 15: 18.4}, {5: 34.4, 9: 42.1},
                             {11: 18.9, 15: 26.7}, {2: 24.5, 6: 31.2, 7: 27.6, 8: 28.9}, {9: 18.9, 11: 23.4, 12: 17.8, 13: 28.9, 15: 30.2}],
communication_time_matrix11 = [[INF, 0, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF],
                               [INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, 0, 0, INF, 0],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]],
in_OR11 = [(9, 10, 11, 12)],

""" job12 """
computation_time_matrix12 = [{3: 21.3, 6: 35.6, 8: 17.8, 13: 18.3}, {1: 6.7, 8: 12.3}, {4: 36.7, 6: 41.2, 14: 32.1, 15: 41.2},
                             {13: 21.8, 14: 14.6, 15: 11.9}, {7: 14.5, 8: 16.7, 9: 25.6, 10: 12.7}, {3: 51.4, 6: 47.8},
                             {12: 6.8, 15: 13.6}, {1: 19.9, 7: 25.6, 9: 21.2}, {4: 26.7, 8: 45.5, 10: 21.5},
                             {6: 19.9, 8: 34.7}, {1: 26.3, 7: 18.1, 14: 31.4}, {2: 9.1, 5: 14.5, 15: 19.6},
                             {1: 16.8, 6: 24.5}, {1: 21.5, 8: 34.5, 13: 20.4}, {5: 28.9, 8: 18.4, 11: 19.7, 13: 23.5}],
communication_time_matrix12 = [
                               [INF, 0, INF, INF, INF, 0, INF, INF, 0, INF, INF, INF, 0, 0, INF],
                               [INF, INF, 0, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, 0, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
                               [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                             ],
in_OR12 = [(2, 6, 7, 8, 9, 13, 14, 15)],

output_filename = "min_date.py"
with open(output_filename, 'w') as f:
    f.write("inf = float('inf')\n")
print("start")
# problem = [[9, 11, 12]]
problem = [[9, 11], [2, 6, 8, 10, 12], [1, 2, 4, 7, 9, 12], [2, 3, 6, 7, 9, 10], [2, 5, 8, 9, 10, 11],
           [3, 4, 6, 7, 8, 10], [3, 5, 7, 8, 10, 12], [1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10, 12],
           [2, 3, 5, 7, 8, 9], [4, 6, 7, 8, 9, 10]]
for pro in range(0, len(problem)):
    print(f'pro{pro + 1}', problem[pro])
    targetms = 0  # 不设定目标值的情况
    targetet = INF
    a = []
    b = []
    c = []
    for job in problem[pro]:
        computation_time_matrix = eval(f'computation_time_matrix{job}')
        if isinstance(computation_time_matrix, list):
            a.extend(computation_time_matrix)
        else:
            time_op = computation_time_matrix[0]
            a.extend(time_op)
        communication_time_matrix = eval(f'communication_time_matrix{job}')
        if isinstance(communication_time_matrix, list):
            communication_time_matrix = [communication_time_matrix]
            b.extend(communication_time_matrix)
        else:
            com = communication_time_matrix[0]
            com = [com]
            b.extend(com)
        in_OR = eval(f'in_OR{job}')
        if isinstance(in_OR, list):
            in_OR = [in_OR]
            c.extend(in_OR)
        else:
            OR = in_OR[0]
            OR = [OR]
            c.extend(OR)
# print(a)
# print(b)
# print(c)
    computation_time_matrix, communication_time_matrix, in_OR = final_matrix(a, b, c)
    length = len(computation_time_matrix)

    with open(output_filename, 'a') as f:
        f.write(f'num_operations{pro + 1} = {length},\n')
        f.write(f"computation_time_matrix{pro + 1} = [")
        for idx, item in enumerate(computation_time_matrix, 1):
            if idx % 3 == 1:
                f.write("    ")
            f.write(str(item))
            if idx % 3 == 0 and idx != len(computation_time_matrix):
                f.write(",\n")
            elif idx != len(computation_time_matrix):
                f.write(", ")
            else:
                f.write("],\n")

        f.write(f"communication_time_matrix{pro + 1} = [\n")
        for idx, row in enumerate(communication_time_matrix):
            f.write(" " * 31)  # 添加空格对齐
            f.write("[")
            for i, val in enumerate(row):
                f.write(f"{val}")
                if i < len(row) - 1:
                    f.write(", ")
            f.write("]")
            if idx < len(communication_time_matrix) - 1:
                f.write(",\n")
            else:
                f.write("\n],\n")
        f.write(f"in_OR{pro + 1} = {in_OR},\n")
        f.write("\n")



