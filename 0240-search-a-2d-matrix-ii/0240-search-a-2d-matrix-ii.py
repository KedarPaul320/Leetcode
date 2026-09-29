class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        r = row - 1 
        c = 0

        while r >= 0 and c < col :
            if matrix[r][c] == target :
                return True 
            if matrix[r][c] < target :
                c += 1
            else :
                r -= 1 
        return False 
        