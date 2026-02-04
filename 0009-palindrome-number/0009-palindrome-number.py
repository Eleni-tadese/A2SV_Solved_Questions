class Solution(object):
    def isPalindrome(self, x):
        num=str(x)
        snum=num[::-1]
        return snum==num
   
        