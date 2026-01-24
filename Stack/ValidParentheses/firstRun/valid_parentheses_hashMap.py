from typing import List
from typing import Dict


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False
        """We are going to use a hashMap to pair matching parentheses instead of hard coding, it is a
        beautiful option whenever we having matching elements"""
        closeToOpen : Dict[str, str] = {"}" : "{", "]" : "[", ")" : "("}
        stack : List[str] = []
        for c in s:
            #Is an opening bracket
            if c not in closeToOpen:
                stack.append(c)
            #Else it is a closing bracket
            else:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                    continue
                return False
        if not stack: return True
        return False
print(Solution().isValid("(]"))