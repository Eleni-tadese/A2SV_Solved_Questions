class Solution:
    def findUnion(self, a, b):
       a.extend(b)
       c = set(a)
       return c
