class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = self.findMinIndex(nums)
        leftNums = nums[index:]
        rightNums = nums[:index]
        originNums = leftNums + rightNums
        left = 0
        right = len(originNums) - 1
        while left < right:
            mid = (left + right) // 2
            if originNums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if originNums[left] == target:
            if left + index >= len(nums):
                return left + index - len(nums)
            return left + index
        return -1

    def findMinIndex(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return left
