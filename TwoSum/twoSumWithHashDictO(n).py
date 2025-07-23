from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

            You may assume that each input would have exactly one solution, and you may not use the same element twice.

            You can return the answer in any order.

            """
            
        hash_dict : dict[int, int] = dict()
        solucion_lista : List[int] = []
        for i in range(len(nums)):
            hash_dict[nums[i]] = i
            
        for i in range(len(nums)):
            difference = target - nums[i]
            if(difference in hash_dict and (i != hash_dict[difference])): 
                solucion_lista.append(hash_dict[difference])
                solucion_lista.append(i)
                return solucion_lista
        return solucion_lista
            
            