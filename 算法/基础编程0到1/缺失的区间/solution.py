class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [lower-1] + nums + [upper+1]
        ans = []
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 2:
                # ans.append(f"{nums[i-1]+1}->{nums[i]-1}")
                ans.append([nums[i-1]+1, nums[i]-1])
            
            elif nums[i] - nums[i-1] == 2:
                # ans.append(str(nums[i-1]+1))
                ans.append([nums[i-1]+1, nums[i-1]+1])
                
        return ans
