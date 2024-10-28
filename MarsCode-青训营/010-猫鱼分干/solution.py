def solution(n, cats_levels):
    # Please write your code here
    return -1

if __name__ == "__main__":
    #  You can add more test cases here
    cats_levels1 = [1, 2, 2]
    cats_levels2 = [6, 5, 4, 3, 2, 16]
    cats_levels3 = [1, 2, 2, 3, 3, 20, 1, 2, 3, 3, 2, 1, 5, 6, 6, 5, 5, 7, 7, 4]
    print(solution(3, cats_levels1) == 4)
    print(solution(6, cats_levels2) == 17)
    print(solution(20, cats_levels3) == 35)