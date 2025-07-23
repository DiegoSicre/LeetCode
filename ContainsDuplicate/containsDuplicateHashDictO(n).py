from typing import List
from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        """Given an integer array nums,
        return true if any value appears at least twice in the array, and return false if every element is distinct."""
        
        #Recommended complexity O(n)
        hash_dict : defaultdict[int, int] = defaultdict(int)
        for num in nums:
            if hash_dict[num] != 0: return True
            hash_dict[num] = hash_dict[num] + 1
        return False
    
