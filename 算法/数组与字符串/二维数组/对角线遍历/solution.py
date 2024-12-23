class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        同一斜线上的元素坐标和一致且为偶数，向右上角->[-1, +1]，即x-1, y+1
        同一斜线上的元素坐标和一致且为奇数，向左下角->[+1, -1]，即x+1, y-1

        临界判断：
            向右上角：(先判断列, 防止在右上角时候向右则越界)
                if x == 第一行：[例如1的位置，y+=1 移动到2的位置]
                    y += 1
                elif y == 最后一列：[先判断列，防止越界，例如图中的3的位置，下一步是左下到6，只能x+=1，y+=1会越界]
                    x += 1
                else:
                    x -= 1
                    y += 1
            向左下角：(先判断行, 防止在左下角的时候向下则越界)
                if x == 最后一行：[先判断行，防止越界，例如图中的7的位置，下一步是右上到5，只能y+=1，x+=1会越界]
                    y += 1
                elif y == 第一列：[例如4的位置, x+1移动到7的位置]
                    x += 1
                else:
                    x += 1
                    y -= 1
        """
        res = list()

        m, n = len(mat), len(mat[0]) # 行数 和 列数
        nums = m * n # 元素数
        
        x, y = 0, 0 # 当前元素坐标
        for i in range(nums):
            res.append(mat[x][y])

            if (x + y) % 2 == 0:
                if y == n - 1: # 最后一列
                    x += 1
                elif x == 0: # 第一行
                    y += 1
                else: # 向右上角
                    x -= 1
                    y += 1 
            else:
                if x == m - 1: # 最后一行
                    y += 1
                elif y == 0: # 第一列
                    x += 1
                else:
                    x += 1
                    y -= 1
        return res