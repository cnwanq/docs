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
