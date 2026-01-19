from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #We first iterate to store every index of every number in nums
        index_dict : defaultdict[int, int] = defaultdict()
        result : List[int] = []
        for i in range(0, len(nums)):
            diff : int = target - nums[i]
            if diff in index_dict:
                result.append(i)
                result.append(index_dict[diff])
                return result
            index_dict[nums[i]] = i
        #This takes O(n) time complexity and O(2n) space complexity
        #Now, to know the solution, we need to see if the difference between target and a given number present
        #in nums is also in nums, in that case we return both indices
        
        
    
        return result
print(Solution().twoSum([3,3], 6))
    