class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        right = (row * col)- 1
        left = 0
      

        while left <= right:
            mid = (left + right) // 2
            curr_row = mid // col
            curr_col = mid % col
           
        
            if matrix[ curr_row ][ curr_col] == target:
                return True
            elif matrix[ curr_row ][ curr_col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False 
