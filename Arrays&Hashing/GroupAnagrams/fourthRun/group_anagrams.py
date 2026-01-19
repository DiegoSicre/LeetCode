from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list[str])
        for word in strs: #O(n)
            word_count : List[int] = [0] * 26
            for letter in word: #O(k), constant size of each word
                word_count[ord(letter) - ord("a")] +=1
            anagram_dict[tuple(word_count)].append(word)
        result : List[List[str]] = []
        for list_anagram in anagram_dict.values():
            result.append(list_anagram)
            
        
        return list(anagram_dict.values())