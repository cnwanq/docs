class Solution:
    def judgeCircle(self, moves: str) -> bool:
        point = [0, 0]
        for chr in moves:
            if chr == 'U':
                point[1] += 1
            elif chr == 'D':
                point[1] -= 1
            elif chr == 'L':
                point[0] -= 1
            elif chr == 'R':
                point[0] += 1
        if point == [0, 0]:
            return True
        return False

