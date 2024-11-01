class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal and len(set(s)) < len(s):
            return True
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
        if len(diff) == 2:
            return True if s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]] else False
        else:
            return False
