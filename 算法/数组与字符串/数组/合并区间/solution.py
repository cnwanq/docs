class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        ans = []
        for x in intervals:
            if not ans or x[0] > ans[-1][1]:
                ans.append(x)
            else:
                ans[-1][1] = max(ans[-1][1], x[1])
        return ans