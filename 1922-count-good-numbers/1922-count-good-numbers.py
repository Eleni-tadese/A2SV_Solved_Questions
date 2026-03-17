class Solution:
    def countGoodNumbers(self, n: int) -> int:
       
        result =0
        if n%2 ==0:
            even_count = n//2
            odd_count = n//2
        else:
            even_count= (n+1)//2
            odd_count = (n-1)//2
        # result = (5**even_count * 4**odd_count) % (10**9 + 7)
        result = (pow(5, even_count, (10**9 + 7)) * pow(4, odd_count, (10**9 + 7))) % (10**9 + 7)
        return result