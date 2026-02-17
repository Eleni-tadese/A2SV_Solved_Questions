class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        
    
        for _ in range(4):
            if mat == target:
                return True
            # Rotate mat 90° clockwise
            mat = self.rotate(mat)
        
        return False
    
    def rotate(self, matrix):
        n = len(matrix)
        # Create new matrix for rotated version
        rotated = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                # 90° clockwise rotation formula
                rotated[j][n-1-i] = matrix[i][j]
        
        return rotated