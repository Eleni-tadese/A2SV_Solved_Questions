class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        l=[]
        for matrix in grid:
            for n in matrix:
                if n<0:
                    l.append(n)
        print(l)
        return len(l)

        