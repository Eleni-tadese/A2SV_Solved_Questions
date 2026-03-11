
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r =0 
        for numbers in nums:
            r ^= numbers
        return r