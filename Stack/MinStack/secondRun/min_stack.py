from collections import defaultdict
from typing import List, Tuple


class MinStack:
    #We'll store the elements in tuples (element, current_min), that'll be set at push time
    array_stack : List[Tuple[int, int]]
    
    def __init__(self):
        self.array_stack = []

    def push(self, val: int) -> None:
        if self.array_stack: current_min : int = min(self.array_stack[-1][1], val)
        else : current_min : int = val
        
        self.array_stack.append((val, current_min))

    def pop(self) -> None:
        self.array_stack.pop()

    def top(self) -> int:
        return self.array_stack[-1][0]

    def getMin(self) -> int:
        return self.array_stack[-1][1]
        
