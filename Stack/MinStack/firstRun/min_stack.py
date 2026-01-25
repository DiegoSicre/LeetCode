from collections import defaultdict
from typing import List, Tuple


class MinStack:
    mininum : int
    prev_min_map : defaultdict[int, Tuple[int, int]]
    stack_array : List[int]
    
    def __init__(self):
        self.stack_array = []
        self.prev_min_map = defaultdict(Tuple[int, int]) 
        self.mininum = 0

    def push(self, val: int) -> None:
        #When pushing we gotta see wether minimum is set, if it is None, that means there are no prev mins and this element becomes the min
        if not self.stack_array:
            self.mininum = val
            self.prev_min_map[val] = (1, self.mininum)
        #New element becomes the min
        #In case minimum exists, we gotta chekc wether this new element is the min
        elif val < self.mininum : #New min
            #Only if it is smaller
            self.prev_min_map[val] = (1, self.mininum) #We store 1 appearance and the prev_min
            self.mininum = val #update new min
        elif val in self.prev_min_map: #If it ain't min, but is in the chain of previous mins, we update the count
            count, prev_min = self.prev_min_map[val]
            self.prev_min_map[val] = (count + 1, prev_min) #We update the count
            
            
        self.stack_array.append(val) #We finally add it

    def pop(self) -> None:
        element_to_be_popped : int = self.top()
        if element_to_be_popped in self.prev_min_map:
            count, prev_min = self.prev_min_map[element_to_be_popped]
            
            #Is the min
            if element_to_be_popped == self.getMin():
                #There are more
                if count > 1:
                    #We simply decrease the count
                    self.prev_min_map[element_to_be_popped] = (count -1, prev_min)
                else: #There are no more of this, we need to destroy the entry and update the new min
                    self.mininum = prev_min #In case is the last, we do not worry as getMin won't be called on an empty stack
                    self.prev_min_map.pop(element_to_be_popped)
            
            #Is a repeated prev_min
            else:
                #If it is repeated and in the prev_min, there is another copy under the current min, so we don't need to pop it from the
                #hash_dict, simply remove the key
                #An element will only be removed from the map when it ceases to be the current min
                self.prev_min_map[element_to_be_popped] = (count - 1, prev_min)
        #We have made all the updates in the prev_min_map
        self.stack_array.pop()
            
        #O(1) time and O(n) space if we only push smaller elements to the stack i.e every push creates a new min, storing all of the in the map.
        

    def top(self) -> int:
        return self.stack_array[-1]

    def getMin(self) -> int:
        return self.mininum


print(MinStack())