from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) == 1: return 0

        i : int = 0
        j : int = i + 1
        temporal_bucket : int = 0 #Here we store the water that is going to be added when i get's updated or at the end of the iteration
        result_bucket : int = 0
        blocks_in_between : int = 0
        while j < len(height):
            #i is updated or 
            if height[j - 1] < height[j]:
                #Water can be trapped now
                temporal_bucket = min(height[j], height[i]) * (j - i - 1) - blocks_in_between
                if height[i] <= height[j]:
                    i = j
                    j = i + 1
                    result_bucket += temporal_bucket #In case we need to update the pointer we do, we add the trapped water, and if we are out of bounds we will simply not meet the next condition
                    blocks_in_between = 0
                    temporal_bucket = 0
                    continue
            
            blocks_in_between += height[j]
            j+=1     
        #Here we won't add the temporal accumulated water, as we cannot ensure the blocks in between, however in i we have the las index we have checked in left-right order
       
        stop_index : int = i
        i = len(height) - 1
        j = i - 1
        if i - stop_index <= 1: return result_bucket
       
        #We refresh the variables
        blocks_in_between = 0
        temporal_bucket = 0
        
        #We apply the same algorithm but in reverse order
        
        while j >= stop_index:
            #i is updated or 
            if height[j + 1] < height[j]:
                #Water can be trapped now
                temporal_bucket = min(height[j], height[i]) * (i - j - 1) - blocks_in_between
                #print("I: ", i, "j:", j, "Temporal: ", temporal_bucket)
                if height[i] <= height[j]:
                    i = j
                    j = i - 1
                    result_bucket += temporal_bucket #In case we need to update the pointer we do, we add the trapped water, and if we are out of bounds we will simply not meet the next condition
                    blocks_in_between = 0
                    temporal_bucket = 0
                    continue
            
            blocks_in_between += height[j]
            j-=1  
        #In this case we've exited the array without updating i and therefore we need to increase the result bucket
        return result_bucket
        """The main issue with the area approach is that we are unable to guarantee the blocks in between the valid area
        if when we traverse the array we don't find a pillar having the same or bigger height as the fixed i pillar.
        
        However, if there is more trapped water to be discovered, we could traverse the array using the same strategy but in reverse order,
        for the segment that we weren't able to count, by keeping the last i update and doing the same strat
        but in reverse order from i = n -1 and j = n -2, until the last i pointer"""
        
        
        #Solution is effectively O(n) time and O(1) space, as we aren't using arrays and are just using variables
        #In the worst case we would do two passes, therefore O(2n) = O(n)
    
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))