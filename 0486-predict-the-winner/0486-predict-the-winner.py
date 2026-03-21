class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def recursion(left, right):
            if left == right:
                return nums[right]
            
            pick_left = nums[left] - recursion(left + 1, right)
            pick_right = nums[right] - recursion(left, right - 1)
            
            return max(pick_left, pick_right)
        
        return recursion(0, len(nums) - 1) >= 0