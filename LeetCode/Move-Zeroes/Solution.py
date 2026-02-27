1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        skr =0
7        plh=0
8
9        while skr < len(nums):
10
11            if nums[skr] != 0:
12                nums[skr],nums[plh] = nums[plh],nums[skr]
13
14                plh+=1
15            skr+=1
16