from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        out = []
        if not nums:
            return out

        l = r = nums[0]
        for i in range(1, len(nums)):
            if i+1 >= len(nums):
                if l == r:
                    out.append(str(l))
                else:
                    out.append(str(l) + "->" + str(r))
            else:
                if nums[i] == nums[i-1]+1:
                    r = nums[i]
                else:
                    if l == r:
                        out.append(str(l))
                    else:
                        out.append(str(l) + "->" + str(r))
                    l = r = nums[i]
                        
                        
        
        return out

mySolution = Solution()
print(mySolution.summaryRanges([0,2,3,4,6,8,9]))