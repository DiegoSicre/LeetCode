from collections import defaultdict
from typing import List, Tuple


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

            if len(speed) == 1: return 1
            with_speed : List[Tuple[int, int]] = []         # [(0,50), (1,20), (2,40)]
            
            for i in range(0, len(speed)):
                with_speed.append((position[i], speed[i]))
                
            
            sorted_with_idx = sorted(with_speed, key=lambda x: x[0])
        
            stack : List[Tuple[int, int]] = []
            stack.append(sorted_with_idx[-1])
            #Note that this technique is a monotonic decreasing stack comparison, which is a LeetCode pattern worth learning
            #for when we need to know the previous max o max, or previous min or next min
            for i in range(len(sorted_with_idx) - 2, -1, -1):
                last_fleet : Tuple[int, int] = stack[-1]
                current_car : Tuple[int, int] = sorted_with_idx[i]
                time_last_fleet = (target - last_fleet[0]) / last_fleet[1]
                time_current_car = (target - current_car[0]) / current_car[1]
                #print("Last Fleet", last_fleet, " Time last fleet: ", time_last_fleet)
                #print("Current car", current_car, " Time current car: ", time_current_car)
                
                if time_current_car <= time_last_fleet:
                    continue
                else: stack.append(sorted_with_idx[i])
            return len(stack)
           # O(n) space due to sorting and usage of the stack
           # O(nlogn) time due to sorting, however, once sorting is done, the algorithm runs in O(n)
        
print(Solution().carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
            
            