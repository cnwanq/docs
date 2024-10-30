class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict = {}
        for c in s:
            if c in dict.keys():
                dict[c] += 1
            else:
                dict[c] = 1
        for c in t:
            if c not in dict.keys() or dict[c] == 0:
                return False
            else:
                dict[c] -= 1
        return True
