class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result = 0
        if 0 in nums:
            return 0
        result = 1
        for i in range(len(nums)):
            if nums[i] < 0:
                result *= -1
        return result
