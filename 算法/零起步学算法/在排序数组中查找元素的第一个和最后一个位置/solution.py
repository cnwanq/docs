class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        if length == 0:
            return [-1, -1]
        first = self.searchFirstRage(nums, target)
        last = self.searchLastRange(nums, target)
        
        return [first, last]
    
    def searchFirstRage(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target and (mid == 0 or nums[mid-1] != target):
                return mid
            elif nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    
    def searchLastRange(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target and (mid == len(nums)-1 or nums[mid+1] != target):
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
