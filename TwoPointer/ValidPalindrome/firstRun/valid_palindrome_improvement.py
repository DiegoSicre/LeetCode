class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #Lets use two pointers to solve the problem in O(n)
        
        """The idea is the following, let's use two pointers simultaneously, until the index is the same we will:
        
        Advance the pointers in left-right order:
        
        -Right pointer moves after left pointer moves:
        a) if char is non alphanumeric -> skip
        b) if char is space -> skip
        c) if char is alphanumeric -> convert to lowercase and wait for comparison
            c.1) if chars are equal -> continue
            c.2) else return False
        d) if indices are the same, it is a palindrome -> return True"""
        if len(s) == 0: return True
        
        i : int = 0 #Left pointer
        j : int = len(s) - 1
        i_char : str = s[i]
        j_char : str = s[j]
        while (i < j): #When they are the same it is a palindrome
            """Instead of using flags to wait, we'll simply check first wether left is to be compared, advance
            it until it is to be compared, and then advance right until it is to be compared
                """
            #Left pointer
            i_char = s[i]
            while not i_char.isalnum():
                i+= 1
                if i >= len(s): return True #If we get out of bounds, that means every single character has passed the test 
                i_char = s[i]
            #So if it is a space, or a non-alnum it'll move forward
            
            #In case i is blocked and j is not, so we need to move j
            j_char = s[j]
            while not j_char.isalnum():
                j-= 1
                if j < 0: return True #If we get out of bounds, that means every single character has passed the test
                j_char = s[j]
            #If it is alnum we convert to lower just in case and we wait
            
            #Both are waiting we do the comparison
            if j_char.lower() == i_char.lower():
                j-=1
                i+=1
                continue
            else: return False
            #We move both pointers
        #If we get out of the loop then it is a palindrome
        return True
                
                
print(Solution().isPalindrome("  "))
            
        