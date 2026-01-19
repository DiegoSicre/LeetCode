from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result : List[int] = [1] * len(nums)
        
        left_acc : int = 1
        #First iteration O(n): right -> left
        for i in range(0, len(nums)):
            result[i] = left_acc #In each cell of the solution array we store the accumulated left product except self
            left_acc *= nums[i] #In each step we store in this variable the accumulated left product at this point

        right_acc : int = 1
        #Second iteration O(n): left->right
        for i in range(len(nums) - 1, -1, -1):
            #This time, as we have stored in each cell the accumulated left product except self, we
            #multiply it by the accumulated right product except self
            result[i] *= right_acc
            right_acc *= nums[i]
        
        return result
    
