from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """Given an array of strings strs, group the

        together. You can return the answer in any order."""

        sol_hash_dict: defaultdict[tuple[tuple[str, int], ...], List[str]] = defaultdict(list)
        for word in strs:
            #As words have a maximum length of 100, iterating through them is O(k)
            hash_dict : defaultdict[str, int] = defaultdict(int)
            for letter in word:
                hash_dict[letter] = hash_dict[letter] + 1
                
            #We have the count, but it is unsorted, and so we want to sort it
            #and turn it into a tuple of sorted pairs
            hashable_tuple = tuple(sorted(hash_dict.items()))  # type: ignore
            sol_hash_dict[hashable_tuple].append(word)
        
        return list(sol_hash_dict.values())