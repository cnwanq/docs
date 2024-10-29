class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = 0
        right = len(s)
        while right > 0:
            chr = s[right-1:right]
            right -= 1
            if chr == ' ':
                if n == 0:
                    continue
                else:
                    break
            elif chr != ' ':
                n += 1
        return n