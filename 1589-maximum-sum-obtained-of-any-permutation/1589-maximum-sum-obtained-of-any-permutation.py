class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        freq = [0] * (n + 1)
        for start, end in requests:
            freq[start] += 1
            freq[end + 1] -= 1
        
        for i in range(1, n):
            freq[i] += freq[i - 1]
        freq.pop()
        nums.sort()
        freq.sort()
        total_sum = 0
        for i in range(n):
            if freq[i] == 0: continue
            total_sum = (total_sum + nums[i] * freq[i]) % MOD
            
        return total_sum