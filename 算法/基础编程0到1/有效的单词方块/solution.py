# Python3 模拟，依据题意遍历模拟，比较第 k 行 和 第 k 列字符串是否相等即可。
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        collen = len(words[0])
        rowlen = len(words)
        for j in range(collen):
            col = ''
            for i in range(rowlen):
                if j < len(words[i]):
                    col += words[i][j]
            if col != words[j]:
                return False
        return True