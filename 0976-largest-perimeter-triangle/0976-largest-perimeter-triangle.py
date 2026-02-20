class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        # Triangle Inequality Theorem.
        # Perimeter = a + b + c, largest we need so we need to sort
        nums.sort()
        
        for i in range(len(nums)-1,1,-1):
            if nums[i-2] + nums[i-1] > nums[i]:
                return nums[i-2] + nums[i-1] + nums[i]
        return 0
    
  