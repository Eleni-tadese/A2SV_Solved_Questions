class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle =[1]
        for i in range (rowIndex):
            rows = [0] *  (len(triangle)+1)

            for j in range(len(triangle)):
                rows[j] += triangle[j]
                rows[j+1] += triangle[j]
            triangle= rows

        return triangle
        