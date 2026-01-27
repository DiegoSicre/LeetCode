from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i : int = 0
        j : int = len(height) - 1
        max_area : int = 0
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            
            #The next index move will substract 1 unit of x length, therefore the maximum solution can only be achieved by moving the index of the pillar with less height
            if height[i] <= height[j]:
                i+=1
            else:
                j-=1
        return max_area
    #O(1) space, no extra, and O(n) time in the worst case as we do only One pass