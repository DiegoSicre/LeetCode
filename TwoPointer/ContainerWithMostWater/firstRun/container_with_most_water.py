from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """We are going to use the two pointer technique, in order for this technique to work,
        we need a decision criteria.
        First of all, we start at maximum x distance, meaning i=0 and j=n-1
        whenever we decide to move a pointer, we know for a fact that the x distance will become smaller.
        
        Therefore what we'll do is: we store the current max area and we only move the smaller height index.
        Because x will get smaller and therefore we know for a fact that a bigger area is only possible if we find 
        another pillar higher or equal than the current bigger one.
        
        In case both pilars are the same height, it does not matter which one to move
        as the previous height will act as a lower bound while x decreases,
        the only way to improve is by finding another taller pillar,
        which we'll find in case it exists in the next movements"""
        
        
        i : int = 0
        j : int = len(height) - 1
        max_area : int = (j - i) * min(height[i], height[j])
        #We know n is at least 2
        while i < j: 
            current_area = (j - i) * min(height[i], height[j])
            max_area = max(max_area, current_area)
            #print("I:", i, "J:", j, "max area:", max_area)
            #Pointer movement
            if height[i] > height[j]:
                j-=1
            elif height[i] <= height[j]:
                i+=1
        return max_area
print(Solution().maxArea([1,1]))
            
    