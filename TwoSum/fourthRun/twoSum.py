from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #We first iterate to store every index of every number in nums
        index_dict : defaultdict[int, List[int]] = defaultdict(list)
        for i in range(0, len(nums)):
            index_dict[nums[i]].append(i)
        #This takes O(n) time complexity and O(2n) space complexity
        #Now, to know the solution, we need to see if the difference between target and a given number present
        #in nums is also in nums, in that case we return both indices
        
        result : List[int] = []
        for n in nums:
            diff : int = (target - n)
            if diff in index_dict and (len(index_dict[n]) > 1 or diff != n):
                
                result = result + index_dict[n]
                if n != diff: result = result + index_dict[diff]
                return result
        #This will take (in the worst case) O(n) time complexity and O(2) space complexity
        #Total complexity O(2n) time and O(2n) space
        return result
print(Solution().twoSum([3,3], 6))
    