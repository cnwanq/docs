from collections import deque

class MyQueue: # 单调队列 从大到小
    def __init__(self):
        self.queue = deque()

    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.popleft()

    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    def front(self):
        return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        window, res = [], []
        for i, x in enumerate(nums):
            if i >= k and window[0] <= i-k:
                window.pop(0)
            while window and nums[window[-1]] <= x:
                window.pop()
            window.append(i)
            if i >= k-1:
                res.append(nums[window[0]])
        return res

        # que = MyQueue()
        # result = []
        # for i in range(k):
        #     que.push(nums[i])
        # result.append(que.front())
        # for i in range(k, len(nums)):
        #     que.pop(nums[i-k])
        #     que.push(nums[i])
        #     result.append(que.front())
        # return result
    #     if len(nums) == 1:
    #         return nums
    #     result = []
    #     left = 0
    #     right = k
    #     while right <= len(nums):
    #         sub_nums = nums[left:right]
    #         max = self.maxNum(sub_nums)
    #         result.append(max)
    #         left += 1
    #         right += 1

    #     return result
        

    # def maxNum(self, nums: List[int]) -> int:
    #     res = nums[0]
    #     for i in range(len(nums)):
    #         if nums[i] > res:
    #             res = nums[i]
    #     return res
        