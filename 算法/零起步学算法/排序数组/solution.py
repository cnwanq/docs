class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length):
            minIndex = i
            for j in range(i + 1, length):
                if nums[j] < nums[minIndex]:
                    minIndex = j
            if minIndex != i:
                nums[i], nums[minIndex] = nums[minIndex], nums[i]
        return nums
