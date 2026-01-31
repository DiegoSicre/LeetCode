from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2: return 0

        i : int = 0
        j : int = len(height) - 1
        #We start at maximum x, and we move the shortes to find a solution in O(n) time and O(1) space, as no data structure is needed
        max_area : int = 0
        while i < j:
            max_area = max(max_area, (j - i) * min(height[i], height[j]))

            if height[i] <= height[j]: i+=1
            else: j-=1
            
        
        return max_area

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))