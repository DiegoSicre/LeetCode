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
        i_waiting : bool = False
        j_waiting : bool = False
        i_char : str = ""
        j_char : str = ""
        while (i < j): #When they are the same it is a palindrome
            
            #Left pointer
            if not i_waiting:
                i_char = s[i]
                if i_char == " ": #If it is a space we skip
                    i+= 1
                    continue
                elif not i_char.isalnum(): #If it is not alphanumeric we skip
                    i+=1
                    continue
                else: #If it is alnum we convert to lower just in case and we wait
                    i_char = i_char.lower()
                    i_waiting = True
            elif i_waiting and not j_waiting:#In case i is blocked and j is not, so we need to move j
                j_char = s[j]
                if j_char == " ": #If it is a space we skip
                    j-= 1
                    continue
                elif not j_char.isalnum(): #If it is not alphanumeric we skip
                    j-=1
                    continue
                else: #If it is alnum we convert to lower just in case and we wait
                    j_char = j_char.lower()
                    j_waiting = True
            else: #Both are waiting we do the comparison
                if j_char == i_char:
                    j_waiting = False
                    i_waiting = False
                    j-=1
                    i+=1
                    continue
                else: return False
                    #We move both pointers
        #If we get out of the loop then it is a palindrome
        return True           
                
                
            
print(Solution().isPalindrome(" "))
            
        