from typing import List
from typing import Dict


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False
        stack : List[str] = []
        close_to_open : Dict[str, str] = {"}" : "{", ")" : "(", "]" : "["}
        #We only receive brackets
        for character in s:
            if character not in close_to_open: #it is an opening bracket
                stack.append(character)
            else:
                if not stack or stack.pop() != close_to_open[character]: return False
        
        
        return not stack