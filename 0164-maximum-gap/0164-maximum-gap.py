class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        l=[]
        if len(nums)<2:
            return 0
        for i in range(1,len(nums)):
            l.append(nums[i]-nums[i-1])
        # print(l)
        return(max(l))
        