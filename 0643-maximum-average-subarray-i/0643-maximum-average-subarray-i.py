class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum =float("-inf")
        cur_sum=0
        avg = max_sum/len(nums)


        # calculating sum for first sub array    # 
        for i in range(k):
            cur_sum += nums[i]
        max_sum = cur_sum

        left =0
        for right in range(k,len(nums)):
            cur_sum -= nums[left]
            cur_sum +=nums[right]

            left += 1

            max_sum =max(max_sum,cur_sum)

        return max_sum/k
