1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        
4        arr = sorted(set(nums))
5        n = len(arr)
6        for i in range(n):
7            nums[i] = arr[i]
8        return n
9
10
11