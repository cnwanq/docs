# 法一：在[0...arr中最大值] 中不断二分，试value，直到找到和正好大于等于target的数
# 然后value-1，得到的数一定小于target，比较这两个数
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        left, right = 0, max(arr)

        def calculateSum(threshold) :
            total = 0
            for num in arr :
                total += min(num, threshold)
            return total

        while left < right :
            mid = left + ((right-left)>>1)
            total = calculateSum(mid)
            if total < target :
                left = mid + 1
            else : right = mid

        sum1 = calculateSum(left-1)
        # value为left时，arr和一定大于等于target
        sum2 = calculateSum(left)
        if target - sum1 <= sum2 - target : return left - 1
        return left