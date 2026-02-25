class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[:k])
        max_sum = summ
        j = 0
        for i in range(k,len(nums)):
            summ -= nums[j]
            summ += nums[i]
            j+=1
            max_sum = max(max_sum,summ)

        return max_sum/k


