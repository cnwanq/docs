class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        :type k: int
        :type nums: List[int]
        """
        # self k
        self.k = k
        self.heap = nums
        # heap其实就是个list
        heapq.heapify(self.heap)
        # 减小到k
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        """
        :type val: int
        :rtype: int
        """
        # 不过堆不够，则直接添加进去
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif self.heap[0] < val:
            # 新的值更大，更新
            heapq.heapreplace(self.heap, val)

        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)