from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

            You may assume that each input would have exactly one solution, and you may not use the same element twice.

            You can return the answer in any order.

            """
            
        hash_dict : dict[int, int] = dict()
        list_sol : List[int] = []
        for i in range(len(nums)):
            difference = target - nums[i]
            if(difference in hash_dict and (hash_dict[difference] != i)):
                list_sol.append(hash_dict[difference])
                list_sol.append(i)
                return list_sol
            
            hash_dict[nums[i]] = i
            
      
        return list_sol
            
            