class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        c1=Counter(s)
        c2=Counter(t)
        print(c1)
        print(c2)
        if c1 ==c2:
            return True
        else:
            return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        