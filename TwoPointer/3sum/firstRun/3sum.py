from typing import List, Set


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """The idea behind this solution is:
        given the relatively small size of the nums array, we'll be turning this problem into
        n two sum sorted problems, leading to a O(n^2) complexity that is optimal for this problem and 
        better than the O(n^3) brute force solution.
        Space could be O(1) but in python sort() can take upto O(n) space"""
        
        
        result : List[List[int]] = []
        #We sort nums in O(nlogn)
        nums.sort() 
        for i in range(0, len(nums)):
            
            target : int = - nums[i] #The target of the subproblem is the opposite of nums[i]
            if i - 1 >= 0 and nums[i] == nums[i - 1]: continue
            j : int = i + 1
            k : int = len(nums) - 1
            while j < k:
                
                if nums[j] + nums[k] < target: #In case the sum is smaller we may increase it by increasing j
                    j+=1
                elif nums[j] + nums[k] > target:#In case the sum is bigger we may decrease it by decreasing k
                    k-=1
                elif nums[j] + nums[k] == target: #In case the sum is what we are looking for we add it to the solutions and we
                    #move both indexes as no further unique combinations will be made with those numbers
                    result.append([nums[i], nums[j], nums[k]]) # We append the solution
                    
                    #We increase j by one
                    
                    j+=1
                    
                    #In case nums[j] is equal to nums[j + 1] we move the index till this is no longer the case, to avoid duplicates
                    while j + 1 < k and nums[j] == nums[j - 1]:
                        
                        j+=1
                        
                    #We mirror it for k
                    k-=1
                    while j < k -1 and nums[k] == nums[k + 1]:
                        k-=1
                    
            
        return result
print(Solution().threeSum([-2,0,1,1,2]))