from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """The idea is that we are going to use two pointers.
        current_sum = numbers[i] + numbers[j].
        
        Three scenarios are possible:
        a)current_sum < target => Increase i
        b)current_sum > target => Decrease j
        c)current_sum == target => return [i + 1, j + 1]
        """
        
        i : int = 0
        j : int = len(numbers) - 1
        
        while numbers[i] + numbers[j] != target:
            #We use the stopping while condition to stop when solution is found
            if numbers[i] + numbers[j] < target: #In case current sum is lower than target, we increase the lower index
                i+=1
            elif numbers[i] + numbers[j] > target: #In case current sum is bigger, we decrease the higher index
                j-=1
        return [i + 1, j + 1]
    
print(Solution().twoSum([-1, 0], -1))