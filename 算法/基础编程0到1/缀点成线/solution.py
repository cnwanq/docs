from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 3:  # 如果坐标点少于3个，无需判断，直接返回True
            return True
        
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        
        # 检查x1和x2是否相等，以避免除以零
        if x1 == x2:
            # 如果所有点的x坐标都相同，那么它们一定在一条直线上
            for x, y in coordinates[2:]:
                if x != x1:
                    return False
            return True
        
        # 使用斜率公式计算两点之间的斜率
        slope = (y2 - y1) / (x2 - x1)
        
        # 从第三个点开始检查是否所有点都在同一直线上
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            # 如果当前点与前两点的斜率不同，则返回False
            if (y - y2) != slope * (x - x2):
                return False
        
        # 如果所有点都在同一直线上，则返回True
        return True