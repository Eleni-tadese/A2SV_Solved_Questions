class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s =0
        p=0
        # [0,1,0,3,12]
        # sp 
        while s<len(nums):
            if nums[s] != 0:
                nums[p] , nums[s] =nums[s],nums[p]
                s+=1
                p+=1
            else:
                s+=1
                
        