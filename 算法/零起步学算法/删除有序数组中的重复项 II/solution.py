class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 2
        if len(nums) < k:
            return len(nums)
        slow = fast = k
        while fast < len(nums):
            if nums[slow - k] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
