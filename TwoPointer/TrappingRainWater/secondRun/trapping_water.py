from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        #Function to calculate the trapped water when we find a pillar >= (j - i - 1) * min(height[i], height[j]) - blocks in between
        
        if len(height) < 3: return 0
        
        
        i : int = 0
        j : int = 1
        trapped_water : int = 0
        blocks_in_between : int = 0
        #First pass O(n)
        #i will only be updated whenever heigh[j] >= heigh[i]
        while j < len(height):
            if height[j] >= height[i]:
                
                trapped_water += (j - i - 1) * min(height[i], height[j]) - blocks_in_between
                blocks_in_between = 0
                i = j
                j = i +1
            else:
                blocks_in_between += height[j]
                j += 1
        
        if i == len(height) - 2: return trapped_water
        blocks_in_between = 0
        limit : int = i
        i = len(height) - 1
        j = i - 1
        
        while j >= limit:
            if height[j] >= height[i]:
                trapped_water += (i - j - 1) * min(height[i], height[j]) - blocks_in_between
                blocks_in_between = 0
                i = j
                j = i - 1
            else:
                blocks_in_between += height[j]
                j -= 1
        return trapped_water
    #Worst case solution is O(n) time as we are doing two passes and  O(1) space
print(Solution().trap([4,2,0,3,2,5]))