from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Given an integer array nums and an integer k, return the k most frequent elements. You may return 
        the answer in any order.

 

        Example 1:

        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]

        Example 2:

        Input: nums = [1], k = 1
        Output: [1]

        

        Constraints:

            1 <= nums.length <= 105
            -104 <= nums[i] <= 104
            k is in the range [1, the number of unique elements in the array].
            It is guaranteed that the answer is unique.
        """
        
        
        #First, as 10-⁴ < nums [i] < 10⁴, I need to count them with a default dict
        
        count_hash_dict : defaultdict[int, int] = defaultdict(int)
        maximum : int = 0
        for num in nums:
            count_hash_dict[num]+=1
            if(count_hash_dict[num] > maximum):
                maximum = count_hash_dict[num]
        #If we use bucket sort instead of using a second hash_dict we use an array
        """count_hash_dict_inverse : defaultdict[int, List[int]] = defaultdict(list[int])
        
        for key,v in count_hash_dict.items():
            count_hash_dict_inverse[v].append(key)"""
        
        print(count_hash_dict)
        frequency_array = [[] for _ in range(maximum)]

        #As the maximum possible number of appearances is n i.e the element appears in every position of the array
        #We can create n bukets 
        #Note: as array indexes go from 0 to 1 we need to move the postion one to the left, i.e, 
        #Position n -1 represents n ocurrences
        
        for key, v in count_hash_dict.items():
 
            frequency_array[v - 1].append(key)
        

        k_added_elements : int = 0
        i : int = maximum - 1 
        sol : List[int] = []
        #Return k elements O(k) worst case O(n)
        while(k_added_elements != k):
               
            sol = sol + frequency_array[i]
            k_added_elements = len(sol)      
            i-=1
        return sol
        
        #Total time complexity O(3n)
        
        
print(Solution().topKFrequent([1,1,1,2,2,3], 2))