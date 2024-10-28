class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums) - 1
        
        while left < right:
            mid = left + (right - left ) // 2
            # 计数， 找小于等于mid的个数
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            # 根据鸽巢原理, https://baike.baidu.com/item/抽屉原理/233776?fromtitle=鸽巢原理&fromid=731656&fr=aladdin
            # <= 说明 重复元素再右半边
            if cnt <=  mid:
                left  = mid + 1
            else:
                right = mid
        return left