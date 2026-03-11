class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        minnum,maxnum=0,int(c**0.5)
        while minnum<=maxnum:
            squares = (minnum**2) + (maxnum**2)

            if  squares > c:
                maxnum-=1
            elif squares < c:
                minnum+=1
            else:
                return True
        return False

        