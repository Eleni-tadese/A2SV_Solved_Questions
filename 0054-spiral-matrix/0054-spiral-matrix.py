class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while left <= right and top <= bottom:

            for i in range(left, right + 1):  #0,3
                result.append(matrix[top][i]) #1, 2, 3
            top += 1

            print(result)
            for i in range(top, bottom + 1): #1,3
                result.append(matrix[i][right])  #6,9
            right -= 1 #1

            print(result)

           
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            print(result)

           
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])   # 9, 8, 7
                left += 1
            print(result)

        return result