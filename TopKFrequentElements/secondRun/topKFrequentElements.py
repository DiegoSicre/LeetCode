from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #We have an array an array of nums, we need to return an array with the k most frequent elements
        frequency_dict : defaultdict[int, int] = defaultdict(int)
        result : List[int] = []
        #We'll iterate thje nums list counting the number of appearances
        max_number_of_appearances : int = 0
        for num in nums:
            frequency_dict[num]+=1
            if(frequency_dict[num]> max_number_of_appearances): max_number_of_appearances+=1
        #Time complexity of this operation is O(n)
        #Space complexity is O(n) in the worst case scenario, every element appears exactly one time
        #After iterating the whole list we need to return the k most frequent elements, note
        #We do a "bucket sort"
        bucket_sort_dict: defaultdict[int, List[int]] = defaultdict(list)
        for key,v in frequency_dict.items():
            bucket_sort_dict[v].append(key)
        #Time complexity O(2n) and space O(2n)
        for i in range(max_number_of_appearances, 0, -1):
            result = result + bucket_sort_dict[i]
            if len(result) == k: return result
            
        return result

print("Solution", Solution().topKFrequent([1,1,1,2,2,3], 2))
            
        
print("Solution", Solution().topKFrequent([1,1,1,2,2,3], 2))
            
        