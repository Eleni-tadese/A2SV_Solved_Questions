class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        l=[]
        if num % 3 ==0:
            x=num//3
            x1=x-1
            x2=x+1
            l.append(x1)
            l.append(x)
            l.append(x2)
        return l