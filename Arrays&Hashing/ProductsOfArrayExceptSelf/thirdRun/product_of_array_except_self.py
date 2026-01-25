from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result : List[int] = [1] * len(nums)
        
        #First pass we accumulate in result the left-prefix product l-r
        acc_product : int = 1
        
        for i in range(0, len(nums)):
            result[i] = acc_product
            acc_product *= nums[i]
            
        #O(n) we store the suffix of nums[i] in every result[i]
        
        #Second pass r-l, we do the same in inverse order
        acc_product = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= acc_product
            acc_product *= nums[i]
        return result
    
    #O(1) space as we are using the necessary result array to store the suffixes and prefixes and O(n) time complexity as we only do two passes