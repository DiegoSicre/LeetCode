from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #First by means of a defaultdict we'll count the frequency of every number, making the key the number and the value the amount of times it has appeared
        
        frequency_dict : defaultdict[int, int] = defaultdict(int) #O(1) insertion and look up by key
        #max frequency tracking to improve complexity
        max_frequency : int = 0
        for n in nums:
            frequency_dict[n]+=1
            max_frequency = max(max_frequency, frequency_dict[n])
        #This takes O(2n) space and O(n) time
        
        #Then, by means of an n-sized array we'll perform a bucket sort
        #where bucket[i] is the list of numbers appearing i times, as we know the range is between [1, n] i.e bounded
        #0(2n) space
        bucket: List[List[int]] = [[] for _ in range(max_frequency)]

       
        for number, frequency in frequency_dict.items():
            bucket[frequency - 1].append(number) #Offset by 1 so i = 0 is 1 time n -1 is n times and so on
        result : List[int] = []
        
        #We return the k most frequent elements, worst case O(n) time if every element is unique and O(k) space
        for index in range(max_frequency - 1, -1, -1):
            result += bucket[index]
            if len(result) == k: return result
        return result

        #O(n) time and space
print(Solution().topKFrequent([1,1,1,2,2,3], 2))