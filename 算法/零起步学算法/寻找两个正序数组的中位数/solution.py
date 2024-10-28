class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        length = len(nums)
        if length % 2 == 0:
            return (nums[length // 2] + nums[(length - 1) // 2]) / 2
        else:
            return nums[length // 2]
        
        