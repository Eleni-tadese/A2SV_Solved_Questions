class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            counts= Counter(nums)
            dominant = -1
            total_count = 0

            for k, v in counts.items():
                if v > len(nums)// 2:
                    dominant = k
                    total_count = v
                    break
            if dominant == -1:
                return -1
            l_count=0
            for i in range(len(nums) - 1):
                if nums[i] == dominant:
                    l_count += 1
            
                right_count = total_count - l_count
                
                if l_count > (i + 1) // 2 and right_count > (len(nums) - i - 1) // 2:
                    return i

        return -1
    
      