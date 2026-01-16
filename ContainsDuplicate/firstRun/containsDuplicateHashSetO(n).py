from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        """Given an integer array nums,
        return true if any value appears at least twice in the array, and return false if every element is distinct."""
        
        #Recommended complexity O(n)
        #If we do it with a hashSet we don´t need to use that much space and time complexity becomes lower
        hash_set : set[int] = set()
        for num in nums:
            if(num in hash_set): return True
            hash_set.add(num)
        return False
    
