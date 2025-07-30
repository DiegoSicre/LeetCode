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
                sol += word
                sol += Solution().convert_length_to_3_digit_string(str(word_length))
                
            return sol
        #As the words have a maximum of 200 characters we need to mark the length of each word with a 3 digit number
        
        def convert_length_to_3_digit_string(self,length : str) -> str:
            while(len(length) < 3):
                new_length : str = "0"
                length =  new_length + length
            return length
        
        
        
        def decode(self, s: str) -> List[str]:
            i : int = len(s) -1
            sol : List[str] = []
            while(i > 0):
                #Here we gotta take the first three letters starting from the left
                num = int(s[i - 2:i + 1])
                #Here we got the amount of  characters the first word starting from the back has
                word : str = s[i - (2 + num):i - 2]
                sol.insert(0, word)
                #Here we have the full word and we gotta update the pointer
                
                
                i -= 3 + num
            return sol
print(Solution().decode(Solution().encode(["neet","code","love","you"])))

#print(Solution().convert_3_digit_string_to_int("333"))
s : str = "033"

#s_int : int = int(s[len(s) -1 : len(s) - 4])
