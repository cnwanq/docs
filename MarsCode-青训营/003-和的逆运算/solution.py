def solution(n, sums):
    # Please write your code here
    return "-2"

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution(3, [1269, 1160, 1663]) == "383 777 886")
    print(solution(3, [1, 1, 1]) == "Impossible")
    print(solution(5, [226, 223, 225, 224, 227, 229, 228, 226, 225, 227]) == "111 112 113 114 115")
    print(solution(5, [-1, 0, -1, -2, 1, 0, -1, 1, 0, -1]) == "-1 -1 0 0 1")
    print(solution(5, [79950, 79936, 79942, 79962, 79954, 79972, 79960, 79968, 79924, 79932]) == "39953 39971 39979 39983 39989")