class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n <= 1:
            return False
        for i in range(n // 2, 0, -1):
            if n % i == 0 and s[:i] * (n // i) == s:
                return True
        return False
