class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def isIncreasing(nums: List[int]):
            n = len(nums)
            for i in range(n-1):
                if nums[i+1] - nums[i] < 0:
                    return False
            return True
        def isDescreasing(nums: List[int]):
            n = len(nums)
            for i in range(n-1):
                if nums[i+1] - nums[i] > 0:
                    return False
            return True
        return isIncreasing(nums) or isDescreasing(nums)