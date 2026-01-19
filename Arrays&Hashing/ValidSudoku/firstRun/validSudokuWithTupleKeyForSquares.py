from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict : defaultdict[int, set] = defaultdict(set) #Each key 0-8 represents the row number and the values present there up to that point
        col_dict : defaultdict[int, set] = defaultdict(set) #Each key 0-8 represents the col number and the values present there up to that point
        square_dict: defaultdict[tuple, set] = defaultdict(set) #Each key 0-8 represents the square number and the values present there up to that point
        for row in range (0, 9):
            for col in range(0, 9):
                current_character : str = board[row][col]
                #print("Row", row)
                #print("Col", col)
                #print("Current character", current_character)
                #Valid character verification
                if not self.isOneToNineOrDot(current_character): return False #If character is not valid return False
                if current_character == ".": continue
                #print("Gets through character validation")
                #Duplicate element in row verification
                if current_character in row_dict[row]: return False #If it is already present return False, duplicate
                else: row_dict[row].add(current_character) #Else, we add it to that rows present elements set
                #print("Gets through row validation")
                #Duplicate element in col verification
                if current_character in col_dict[col]: return False
                else: col_dict[col].add(current_character)
                #print("Gets through col validation")
                #Duplicater element in 3x3 box verification
                key = (row//3, col//3)
                if current_character in square_dict[tuple(key)]: return False
                else: square_dict[tuple(key)].add(current_character)
                #print("Gets through square validation and goes onto the next")
        #In case none of the cells was invalid, sudoku is valid and we may return True
        return True    
                
        return True
    def isOneToNineOrDot(self, character : str) -> bool:
        if character == ".": return True
        
        if str.isdigit(character):
            character_converted : int = int(character)
            if character_converted >= 1 and character_converted <= 9: return True
            
        return False

        
        
print(Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))