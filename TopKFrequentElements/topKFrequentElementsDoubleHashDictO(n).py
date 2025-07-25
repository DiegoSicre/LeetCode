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
        #Create an inverse dict that point from k(count) -> v(elements with that count)
        count_hash_dict_inverse : defaultdict[int, List[int]] = defaultdict(list[int])
        
        for key,v in count_hash_dict.items():
            count_hash_dict_inverse[v].append(key)
        
        
        
        k_added_elements : int = 0
        i : int = maximum
        sol : List[int] = []
        #Return k elements O(k) worst case O(n)
        while(k_added_elements != k):
            if(i in count_hash_dict_inverse):   
                sol = sol + count_hash_dict_inverse[i]
                k_added_elements = len(sol)

               
            i-=1
        return sol
        
        #Total time complexity O(3n)
        
        
print(Solution().topKFrequent([1,1,1,2,2,3], 2))