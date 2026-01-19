from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        result_str : str = ""
        for word in strs:
            result_str += str(len(word)) #We add the length, as we have control over the first character of the
            #str, as it will always be ours
            result_str += "#" #Until the first # we are telling the length of the word
            result_str += word
        return result_str
    
    def decode(self, s: str) -> List[str]:
        result : List[str] = []
        i : int = 0
        while i < len(s):
            skip : int = 0
            char : str = s[i]
            while char != "#": #Until we don't find the first separator we are getting the length of the skip
                skip *= 10
                skip += int(char)
                i+=1
                char = s[i]
            #Once we hit the # we need to get the slice and make the jump
            result.append(s[i + 1: i + 1 + skip])
            #Once we have updated the word, we want to update the i pointer to the following length count
            i+= skip + 1
        
        return result

print(Solution().decode(Solution().encode(["Hello", "World"])))