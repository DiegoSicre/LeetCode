from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
       
        """We are going to use a stack, whenever we find an operator, we'll perform the operation
        following a: second extracted (operator) first extracted.
        
        We'll add every element to a stack, when we find an operator we'll perform said operation with the 
        aforementioned order and we'll do so after the array is fully traversed"""
        operators : set[str] = {"+", "-", "/", "*"}
        stack : List[int] = []
        for token in tokens:

            if token not in operators:
                stack.append(int(token))
            else:
                first_operand : int = stack.pop()
                second_operand : int = stack.pop()
                new_operand : int = 0
                if token == "+":
                    new_operand = second_operand + first_operand
                elif token == "-":
                    new_operand = second_operand - first_operand
                elif token == "*":
                    new_operand = second_operand * first_operand
                else:
                    new_operand = int((second_operand / first_operand))
                stack.append(new_operand)
           
        return stack.pop()
        #As we go through every single numeric value twice and through operands once, it is a O(2m + n) problem.
        #I've used a set to check operands as there are only 5 of them, meaning O(k) space.
        #O(n) space due to the stack and O(n) time


print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))