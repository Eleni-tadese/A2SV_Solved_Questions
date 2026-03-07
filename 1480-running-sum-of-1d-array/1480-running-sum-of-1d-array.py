class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pref=[]
        n=len(nums)
        total=0
        for i in range(n):
            total = total + nums[i]
            pref.append(total)
        print(pref)
        return pref