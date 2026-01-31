from typing import List, Tuple


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """The idea we are gonna follow is: we'll store tuples in the stack with 
        (temperature, index).
        
        We'll iterate the temperatures array, and we'll store in result[i] = 0.
        Then we'll pop() the stack until temperatures[i] <= stack[-1].
        
        In every pop() we'll store it result[index] = i - index.
        
        Effectively going through the whole array twice, meaning a O(2n) = O(n) complexity that's way better than 
        the O(n^2) approach and O(n) space complexity for using a stack that in case temperatures is in increasing
        order will store all of it's elements
        """
        
        
        result : List[int] = [0] * len(temperatures)
        if len(temperatures) == 1: return result
        
        stack : List[Tuple[int, int]] = [] #Tuples contain (day_temperature, day_index)
        stack.append((temperatures[0], 0))
        for i in range(1, len(temperatures)):
            while temperatures[i] > stack[-1][0] : #Strictly bigger
                day_index : int = stack.pop()[1]
                result[day_index] = i - day_index
                if not stack: break # This could be avoided by adding a while stack and temperatures[i] > stack[-1][0] to the while condition
            result[i] = 0
            stack.append((temperatures[i], i))
        return result
        
print(Solution().dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))
        
        
        