from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string : str = ""
        for word in strs:
            encoded_string += str(len(word))
            encoded_string += "#"
            encoded_string += word
        return encoded_string
               
               
    
    
    def decode(self, s: str) -> List[str]:
            decoded_array : List[str] = []
            i : int = 0
            while(i < len(s)):
                jump : str = ""
                
                letter : str = s[i]
                while(letter != "#"):
                    jump += letter
                    
                    
                    i += 1
                    letter = s[i]
                
                decoded_array.append(s[i + 1 : i + 1 + int(jump)])
                
                i += int(jump) + 1
                
               
            return decoded_array
                
            
                
print(Solution().decode(Solution().encode(["neet","code","love","you"])))