from typing import List, Set


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #We'll use a set to add elements while traversing and comparing in O(1) is the current element was already there
        #Worst case O(n) time and O(n) space
        
        elements_set : Set[int] = set()
        for n in nums:
            if n in elements_set: return True
            elements_set.add(n)
        return False