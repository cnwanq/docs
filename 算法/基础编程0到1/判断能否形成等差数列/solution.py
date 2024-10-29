class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return True
        arr.sort()
        for i in range(n-2):
            if arr[i+1] - arr[i] != arr[i+2] - arr[i+1]:
                return False
        return True