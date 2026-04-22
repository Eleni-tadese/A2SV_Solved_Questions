class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        last = nums[n - 1]
        ans = 0

        for i in range(n - 2, -1, -1):
            if nums[i] > last:
                num_elements = (nums[i] + last - 1) // last

                ans += num_elements - 1
                last = nums[i] // num_elements
            else:
                last = nums[i]

        return ans
