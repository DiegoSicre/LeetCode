from typing import List, Set


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
       
        nums.sort()
        result : List[List[int]] = []
        for k in range(0, len(nums)):
            if nums[k] > 0: break #
            if k >= 1 and nums[k] == nums[k-1]:
                continue
            
            i : int = k + 1
            j : int = len(nums) - 1 
            target : int = -nums[k]
            while i < j:
                if i > k + 1 and nums[i] == nums[i - 1]:
                    i += 1
                    continue
                if j < len(nums) - 1 and nums[j] == nums[j + 1]:
                    j -= 1
                    continue
                if nums[i] + nums[j] < target:
                    i+=1
                elif nums[i] + nums[j] > target:
                    j-=1
                else:
                    result.append([nums[k], nums[i], nums[j]])
                    i+=1
                    j-=1
        return result             
    
    
print(Solution().threeSum([-1,0,1,2,-1,-4]))