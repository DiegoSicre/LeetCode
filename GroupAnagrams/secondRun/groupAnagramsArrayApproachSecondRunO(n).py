from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        
        """Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

            An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

            Example 1:

            Input: strs = ["act","pots","tops","cat","stop","hat"]

            Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

            Example 2:

            Input: strs = ["x"]

            Output: [["x"]]

            Example 3:

            Input: strs = [""]

            Output: [[""]]

            Constraints:

                1 <= strs.length <= 1000.
                0 <= strs[i].length <= 100
                strs[i] is made up of lowercase English letters.

            """
        hash_dict_grouped_anagrams = defaultdict(list[str])
        for word in strs:
            count : List[int] = [0] * 26
            #As the maximum word lenght is 100 iterating the characters takes constant time O(K)
            for letter in word:
                count[ord(letter) - ord("a")]+= 1
            #As Lists are not hashable we convert it into a tuple
            hash_dict_grouped_anagrams[tuple(count)].append(word)
        
        return list(hash_dict_grouped_anagrams.values())
    
print(Solution().groupAnagrams(["act","pots","tops","cat","stop","hat"]))
                