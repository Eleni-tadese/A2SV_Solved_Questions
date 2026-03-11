class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        
        sorted_nums = sorted(nums)


        first_position = {}

        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in first_position:
                first_position[sorted_nums[i]] = i

        
        result = []
        for num in nums:
            result.append(first_position[num])

        return result

     
