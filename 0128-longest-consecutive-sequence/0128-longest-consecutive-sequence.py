class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set=set(nums)
        longest=0
        for n in my_set:
            if n-1 not in my_set:
                next_n = n+1
                count =1

                while next_n in my_set:
                    count+=1
                    next_n +=1
                longest=max(count,longest)
        return longest
        