class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        counter = 0
        for i in range(left, right + 1):
            for a, b in ranges:
                if i >= a and i <= b:
                    counter += 1
                    break

        
        if counter == right + 1 - left:
            return True
        return False
        