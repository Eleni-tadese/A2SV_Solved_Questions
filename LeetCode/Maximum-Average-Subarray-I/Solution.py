1class Solution:
2    def findMaxAverage(self, nums: List[int], k: int) -> float:
3        
4        window_sum =sum(nums[:k])
5        max_sum =  window_sum
6
7        for r in range(k, len(nums)):
8            window_sum += nums[r]
9            window_sum-= nums[r-k]
10
11            max_sum = max(max_sum , window_sum)
12        
13        return max_sum /k