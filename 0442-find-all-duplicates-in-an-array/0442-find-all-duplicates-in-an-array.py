class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        
        for x in nums:
            val = abs(x)
            index = val - 1
            
         
            if nums[index] < 0:
                result.append(val)
            else:
                nums[index] = -nums[index]
                
        return result