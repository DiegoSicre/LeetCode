class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Main idea is: we strip and remove non-aplhanumeric characters and it reads the same forward and backward
        #By advancing two pointers at the same time verifying that both letters are the same
        
        if len(s) == 1: return True
        
        i : int = 0
        j : int = len(s) - 1
        
        while i < j:
            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            elif s[i].lower() != s[j].lower(): return False
            else:
                i+=1
                j-=1
        return True

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))