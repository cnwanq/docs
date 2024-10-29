class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not str:
            return 0
        j = 1
        max_len = 0
        for i in range(len(s)):
            j = max(j, i+1)
            while j < len(s) and s[j] not in s[i:j]:
                j += 1
            max_len = max(max_len, j-i)
        return max_len
