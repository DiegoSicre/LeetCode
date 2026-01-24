from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False
        
        stack : List[str] = []
        for c in s:
            #Is an opening bracket
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            #Else it is a closing bracket
            else:
                if len(stack) == 0: return False
                if c == ")":
                    if stack[-1] != "(": return False
                    stack.pop()
                    
                    
                elif c == "}":
                    if stack[-1] != "{": return False
                    stack.pop()        
                
                else: #c is "]"
                    if stack[-1] != "[": return False
                    stack.pop()
        if len(stack) == 0: return True
        return False
print(Solution().isValid("(]"))