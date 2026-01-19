from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        #In order to count the frequency of lower case english letters we can use an array of 26 cells
        #cell with index 0 will represent 'a' and the other letters will be represented by the other index numbers in alphabetical order.
        
        #We are going to create a hashDict where they keys are the tupled arrays and the values a list of all the words having that count
        hash_dict : defaultdict[tuple[int, ...], List[str]] = defaultdict(list[str])
        for word in strs:
            count :List[int] = [0] * 26
            #As the max word length is 100 we can iterate the characters in 0(100)
            for char in word:
                count[ord(char) - ord("a")] += 1
                
            hash_dict[tuple(count)].append(word)
            
        return list(hash_dict.values())
    
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))