from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        result : str = ""
        for word in strs:
            result += str(len(word))
            result += "#"    
            result += word
            #we know words have constant time so this is effectively O(1) time        
        return result
    def decode(self, s: str) -> List[str]:
        i : int = 0
        result : List[str] = []
        while i < len(s):
            word_length : int = 0
            while s[i] != "#":
                word_length *= 10
                word_length += int(s[i])
                i+=1
            #Here we are at "#"
            result.append(s[i + 1:i + 1 + word_length])
            i = i + 1 + word_length
        return result
    #O(n) time complexity as we only traverse the str and O(n) space, being n the number of chars in the encoded str length
print(Solution().decode(Solution().encode(["Hello","World"])))
            
                
                