class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        rows, cols = len(mat), len(mat[0])
        result = []
        
        for diagonal in range(rows + cols - 1):
            if diagonal % 2 == 0:  # Even diagonal - traverse upward
                # Start from bottom or right edge
                r = min(diagonal, rows - 1)
                c = diagonal - r
                
                while r >= 0 and c < cols:
                    result.append(mat[r][c])
                    r -= 1
                    c += 1
                    
            else:  # Odd diagonal - traverse downward
                # Start from top or left edge
                c = min(diagonal, cols - 1)
                r = diagonal - c
                
                while c >= 0 and r < rows:
                    result.append(mat[r][c])
                    r += 1
                    c -= 1
        
        return result