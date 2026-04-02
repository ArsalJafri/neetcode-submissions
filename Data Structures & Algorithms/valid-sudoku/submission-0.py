class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
         
        # Iterate over every cell in the board
        for numRow in range(9):
            for numCol in range(9):
                if board[numRow][numCol] == ".":
                    continue  # Skip empty cells
                val = int(board[numRow][numCol]) - 1  # Get the number and adjust for 0-based index
                
                # Check if the current number has already appeared in the current row
                if (1 << val) & rows[numRow]:
                    return False
            
                # Check if the current number has already appeared in the current colum
                if (1 << val) & cols[numCol]:
                    return False
            
                # Check if the current number has already appeared in the current sub-box
                if (1 << val) & boxes[(numRow // 3) * 3 + (numCol // 3)]:
                    return False

                # Update the bitmask for row, column, and sub-box
                rows[numRow] |= (1 << val)
                cols[numCol] |= (1 << val)
                boxes[(numRow // 3) * 3 + (numCol // 3)] |= (1 << val)
        return True
