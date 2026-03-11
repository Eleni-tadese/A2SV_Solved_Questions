class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        divider =1
        while x >= divider * 10:
            divider *= 10
        while x>0:
            l=x//divider
            r= x % 10
            
            if r!=l:
                return False
            x = (x % divider) // 10
            divider //= 100
        return True

     