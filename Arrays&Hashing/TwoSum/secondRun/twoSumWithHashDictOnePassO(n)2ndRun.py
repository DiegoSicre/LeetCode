"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        #Keys to solving this problem, assuming there is only one solution
        #Negative numbers are valid
        #Careful not to add the same index twice
        
        sol : List[int] = []
        hash_dict : defaultdict[int, int] = defaultdict(int)
        
        for i in range(len(nums)):
            difference = target - nums[i]
            if(difference in hash_dict and hash_dict[difference] != i):
                
                return sol + [hash_dict[difference], i]
            hash_dict[nums[i]] = i
        
        return sol
            