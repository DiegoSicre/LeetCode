from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """We are going to use a hashSet, we will store in every step of the iteration the 
        element in the set O(1), and before adding it we will also compare if it was already there O(1).
        If it was there, then we return True, else we keep iterating, after fully iterating the array in
        O(n) we will return False, as that would mean no duplicate was found
        """
        
        duplicate_hash_set : set[int] = set()
        for n in nums:
            if n in duplicate_hash_set: return True
            duplicate_hash_set.add(n)
            
        return False