from typing import List
class Solution:

    

    #def decode(self, s: str) -> List[str]:
        """Encode and Decode Strings

        Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

        Please implement encode and decode

        Example 1:

        Input: ["neet","code","love","you"]

        Output:["neet","code","love","you"]

        Example 2:

        Input: ["we","say",":","yes"]

        Output: ["we","say",":","yes"]

        Constraints:

            0 <= strs.length < 100
            0 <= strs[i].length < 200
            strs[i] contains only UTF-8 characters.


        """
        
        """////MY SOLUTION////
        The key here is that we want to find the way to separate each word in a way were the same string, with other words, couldn't be created.
        The way I have found is to iterate the string we create backwards. When we encode, we include behind each word a number with the amount of
        characters that word has. That way we have control over the last character of the word. That character will always be added by us,
        if we know, starting from that character, that is actually gonna be a 3 digit character, where this word finishes, and where the next one starts
        This works because we know the max length of each word is 200 characters
        
        """
        
        def encode(self, strs: List[str]) -> str:
            #We are given a list of strings
            
            sol : str = ""
            for word in strs:
                word_length : int = len(word)
                sol += str(len(word))
                sol += "#"
                sol += word
                
            return sol
        #As the words have a maximum of 200 characters we need to mark the length of each word with a 3 digit number
        
        def convert_length_to_3_digit_string(self,length : str) -> str:
            while(len(length) < 3):
                new_length : str = "0"
                length =  new_length + length
            return length
        
        
        
        def decode(self, s: str) -> List[str]:
            i : int = 0
            sol : List[str] = []
            while(i < len(s)):
                #So to get the num we iterate till we find the first #
                num : str = ""
                while(s[i] != "#"):
                    num += s[i]
                    
                    i +=1
                word : str = s[i + 1: i + 1 + int(num)] #i + 1 because it starts at the # index
                sol.append(word)
                i += 1 + len(word)
                #We update the i pointer by i + 1 (because we are at # index) + word length
                
            return sol
print(Solution().decode(Solution().encode(["neet","code","love","you"])))


