from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

        You must write an algorithm that runs in O(n) time and without using the division operation.

        

        Example 1:

        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]

        Example 2:

        Input: nums = [-1,1,0,-3,3]
        Output: [0,0,9,0,0]

        

        Constraints:

            2 <= nums.length <= 105
            -30 <= nums[i] <= 30
            The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

        

        Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
        """
        
        #In order to achieve O(1) we are gonna use the result array as the one in which we do operations
        
        #First iteration left-right: acc is the product of the elements at the left except self
        acc_left_product : int = 1
        result : List[int] = [1] * len(nums) #We need to initialize it to 1 so that the product doesn't become 0 or None
        #I am going to perform a regular for loop instead of a for each to access both arrays simultaneously
        for i in range(len(nums)):
            result[i] = acc_left_product
            acc_left_product *= nums[i]
        
        #Second iteration right-to-left
        acc_right_product : int = 1
        #We have in each cell of the result array the product of the elements at the left of nums[i], we are going to multiply that
        # with the accumulated elements at the right as acc-at-left * acc-at-right = product of array except self
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= acc_right_product
            acc_right_product *= nums[i]
        return result
        
print(Solution().productExceptSelf([1,2,3,4]))
            
            
