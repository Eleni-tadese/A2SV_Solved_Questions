class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        l,r=0,len(arr)-1
        new=[]
        for index,value in enumerate(arr):
            new.append([value,index])
        new.sort()
        while l<r:
            if new[r][0]+new[l][0]>target:
                r-=1
            elif new[r][0]+new[l][0]<target:
                l+=1
            else:
                return [new[l][1],new[r][1]]
        # dict = {}
        # for i, num in enumerate(nums):
        #     diffrence = target - num
        #     if diffrence in dict:
        #         return [dict[diffrence], i]
        #     dict[num] = i
# class Solution:
#     def twoSum(self, arr: List[int], target: int) -> List[int]:
#         neww = [[val, idx] for idx, val in enumerate(arr)]
#         neww.sort()   # sort by value
        
#         l, r = 0, len(arr) - 1
        
#         while l < r:
#             s = neww[l][0] + neww[r][0]
            
#             if s == target:
#                 return [neww[l][1], neww[r][1]]
            
#             if s < target:
#                 l += 1
#             else:
#                 r -= 1
