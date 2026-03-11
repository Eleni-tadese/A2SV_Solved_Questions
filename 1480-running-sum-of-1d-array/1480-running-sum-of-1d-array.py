class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        total = 0
        for i in range(n):
            total += nums[i]
            prefix[i] = total
        return prefix
   