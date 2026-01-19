from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """The idea is that we are going to iterate a first time adding every element to a hashset,
        doing so we are able to check wether an element is present in nums in O(1)."""
        #Edge cases, nums has length 0 or 1 (this improves complexity a lot)
        if len(nums) == 1: return 1
        elif len(nums) == 0: return 0
        
        #O(n) adding every element to a set
        hash_set_nums : set[int] = set()
       
        for n in nums:
            
            hash_set_nums.add(n)
            
        
        """Now, the algorithm will check if a number has next or previous and four things can be true
        a) Number doesn't have next nor previous, meaning it isn't part of a sequence, we move on
        b) Number has next but not prev, it is a tail, in this algorithm we will also skip it
        c) Number has next and prev, it is a number in the middle of a sequence, we will also skip it
        d) Number has prev but doesn't have next, it is the head of a sequence, we will count the sequence, this is O(n) in the worst case and we would have found the solution
        """
        max_sequence_length : int = 1 #Due to edge case where there are for example [0, 0], if lenght isn't 0, which we've checked, then it is at least 1
        for n in hash_set_nums: #O(2n) in the worst case 
            
            #Doesn't have previous a) or b)
            if not (n - 1) in hash_set_nums: continue
                
            #Has previous
            else:
                #c)
                if (n + 1) in hash_set_nums: continue
                #d) We count the sequence
                else:
                    current_sequence_lenght : int = 0
                    num_iteration : int = n
                    while (num_iteration in hash_set_nums): #We iterate until the end of the sequence
                        current_sequence_lenght += 1
                        num_iteration -= 1
                    if (current_sequence_lenght > max_sequence_length):
                        max_sequence_length = current_sequence_lenght
        return max_sequence_length
                    
        #O(3n) => O(n) time complexity and O(n) space complexity
                    
                
                