from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Given two strings s and t, return true if t is an of s, and false otherwise."""
        
        """Constraints: 
        1 <= s.length, t.length <= 5 * 104
        s and t consist of lowercase English letters.
        """
        
        
        #Complexity: minimum O(3n), n being the lenght of the word, in case they are equal.
        
        #Different lengths, not an anagram, minimal condition
        if(len(s) != len(t)):
           return False 
       
        #Anagram: word that is obtained by rearranging an other word's letters
        hash_dict_s : defaultdict[str, int] = defaultdict(int)
        hash_dict_t : defaultdict[str, int] = defaultdict(int)
        for letter in s:
            hash_dict_t[letter] = hash_dict_t[letter] + 1
        
        for letter in t: 
            hash_dict_s[letter] = hash_dict_s[letter] + 1
            
            
        if(hash_dict_s != hash_dict_t): return False
        return True