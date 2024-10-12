# # 问题描述

# 油价飞升的今天，我们尽量减少花费。我们出门旅游，有时候租车去旅游也是一种不错的方式。这次我们这次旅游是从「青海湖」到「景点 X」，景点 X 可以是「敦煌」、「月牙泉」等，线路的路径是唯一的，假设我们每走 1 km 消耗 1 L 的油，车油箱容量 400L。比如：如果「景点 X」是敦煌，我们在青海湖租车前油箱是 200L 的，在「景点 X」（敦煌）还车的时候也是 200L 的，路上有很多加油站，加油站在青海湖和「景点 X」的连线上。

# ## 输入格式

# 第 1 行表示「青海湖」到「景点 X」的距离，距离最远不超过 10000 km。
# 第 2 行表示接下来 N 行表示 N 个加油站（N 为正整数）。
# 接下来 N（1 <= N <= 100）行表示，每一个加油站情况。每一个加油站包括距离「景点 X」的距离 a km（0 <= a <= 10000），以及每升汽油的价格 b 元（0 <= b <= 2000），a 和 b 均为正整数。

# ## 输出格式

# 如果不能到达目的地「景点 X」，输出 Impossible。
# 如果能到达目的地「景点 X」，输出最小花费多少元。

# **输入样例**：
# 500
# 4
# 100 1
# 200 30
# 400 40
# 300 20

# **输出样例**：
# 4300

# ## 解题思路
    # 1. 计算出加油站到「景点 X」的距离，并排序
    # 2. 从距离最远（第一个）的加油站开始加油，如果当前油量不足以到达下一个加油站，则继续加油，直到到达最后一个加油站。
    # 3. 如果中途遇到无法到达下一个加油站的场景，则返回 "Impossible"
# ## 代码实现
def solution(distance, n, gas_stations):
    # 花的费用
    total_cost = 0
    # 当前的距离
    current_distance = 0
    # 当前油量
    current_gas = 200  # 假设初始油量为 200L
    # 存储加油站信息的列表
    stations = []
    for gas_station in gas_stations:
        # 计算加油站到「景点 X」的距离
        distance_to_x = distance - current_distance
        # 如果当前距离大于加油站的距离，则继续加油
        if distance_to_x > gas_station[0]:
            current_gas += (gas_station[1] * gas_station[0])  # 加油
            total_cost += (gas_station[1] * gas_station[0])  # 记录费用
            current_distance += gas_station[0]  # 更新当前距离
        else:
            # 如果当前距离小于加油站的距离，则无法到达下一个加油站
            if current_gas < distance_to_x:
                return "Impossible"
            else:
                total_cost += (gas_station[1] * distance_to_x)  # 记录费用
                current_gas -= distance_to_x  # 减去油量
                break
        # 更新当前距离
        current_distance = gas_station[0]
        # 存储加油站信息
        stations.append((gas_station[0], gas_station[1]))
        # 排序加油站信息
        stations.sort(key=lambda x: x[0])
    return total_cost



def solution(distance, n, gas_stations):
    # 花的费用
    total_cost = 0
    # 当前的距离
    current_distance = 0
    # 当前油量
    current_gas = 200  # 假设初始油量为 200L
    # 存储加油站信息的列表
    stations = []


    
    return -1

if __name__ == "__main__":
    #  You can add more test cases here
    gas_stations1 = [(100, 1), (200, 30), (400, 40), (300, 20)]
    gas_stations2 = [(100, 999), (150, 888), (200, 777), (300, 999), (400, 1009), (450, 1019), (500, 1399)]
    gas_stations3 = [(101,), (100, 100), (102, 1)]
    gas_stations4 = [(34, 1), (105, 9), (9, 10), (134, 66), (215, 90), (999, 1999), (49, 0), (10, 1999), (200, 2), (300, 500), (12, 34), (1, 23), (46, 20), (80, 12), (1, 1999), (90, 33), (101, 23), (34, 88), (103, 0), (1, 1)]

    print(solution(500, 4, gas_stations1) == 4300)
    print(solution(500, 7, gas_stations2) == 410700)
    print(solution(500, 3, gas_stations3) == "Impossible")
    print(solution(100, 20, gas_stations4) == 0)
    print(solution(100, 0, []) == "Impossible")
