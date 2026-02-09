class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_nums=[]
        for v,i in enumerate(nums):
            list_nums.append([i,v])
        print(list_nums)

        list_nums.sort()
        l=0
        r=len(nums)-1
       
        while l<r:
            if list_nums[r][0]+ list_nums[l][0]>target:
                r-=1
            elif list_nums[r][0]+ list_nums[l][0]<target:
                l+=1
            else:
                return [list_nums[l][1],list_nums[r][1]]
      