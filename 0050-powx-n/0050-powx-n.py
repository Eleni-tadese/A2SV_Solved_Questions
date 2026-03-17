class Solution:
    def myPow(self, x: float, n: int) -> float:
        # power = x **n
        # return power
        def power(x, n):
            if n == 0:                  
                return 1
            if n < 0:                  
                 return 1 / power(x, -n)
    
            half = power(x, n // 2)      

            if n % 2 == 0:              
                return half * half
            else:                       
                return half * half * x
        return power(x,n)
