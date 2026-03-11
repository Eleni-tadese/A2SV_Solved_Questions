# User function Template for python3
from collections import Counter
class Solution:
    # Function to check if a is a subset of b.
    def isSubset(self, a, b):
        dicta = Counter(a)
        dictb = Counter(b)
        for keys, values in dictb.items():
            if dicta[keys] < values:
                return False
        return True
