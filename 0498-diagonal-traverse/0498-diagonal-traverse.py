class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        m=len(mat)
        n=len(mat[0])

        diagonals=defaultdict(list)

        for i in range(m):
            for j in range(n):
                diagonals[i+j].append(mat[i][j])
        print(diagonals)

        result =[]

        for i in range (m + n - 1):
            if i%2 ==0:
                diagonals[i].reverse()

            result.extend(diagonals[i])
        print(diagonals)

       
        return result

            