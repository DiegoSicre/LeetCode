from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """Given an array of strings strs, group the

        together. You can return the answer in any order."""

        hash_dict : defaultdict[tuple[int, ...], List[str]] = defaultdict(list)
        for word in strs:
            #As words have a maximum length of 100, iterating through them is O(k)
            #hash_dict : defaultdict[str, int] = defaultdict(int)
            #instead of using a hashDict, we are going to use an array of 26 positions
            #where each position i-> represents a letter and the value stored at the postion, represents the ocurrences
            count : List[int] = [0] * 26
            
            for letter in word:
                count[ord(letter) - ord("a")] += 1
                
            #We have the count, and now is sorted
            hashable_tuple = tuple(count)
            hash_dict[hashable_tuple].append(word)
        
        return list(hash_dict.values())