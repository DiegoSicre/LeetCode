from typing import List, Set


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #First pass we add every num to a set to be able to check a number presence in nums in O(1)
        
        if not nums: return 0
        if len(nums) == 1: return 1
        
        set_numbers : Set[int] = set()
        for n in nums:
            set_numbers.add(n)
        
        
        max_sequence_length : int = 0
        #it becomes inneficient when having a lot of duplicates, so we can simply traverse the set
        for n in set_numbers:
            if n - 1 in set_numbers: continue
            else:
                current_sequence_length : int = 1
                #It is the start of a sequence
                current_num : int = n
                while current_num + 1 in set_numbers:
                    current_num+=1
                    current_sequence_length+=1
                max_sequence_length = max(max_sequence_length, current_sequence_length)
        return max_sequence_length
print(Solution().longestConsecutive([100,4,200,1,3,2]))