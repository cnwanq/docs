class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        if n == 1:
            return mat[0][0]
        sum = 0
        for i in range(n):
            sum += mat[i][i]
            j = n-i-1
            if j != i:        
                sum += mat[n-i-1][i]
        return sum