class Solution(object):
    def missingNumber(self, nums):
        setn=set(nums)
        for i in range(len(nums)+1):
            if i not in setn:
                return i
        