class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        c = Counter(nums)

        for i , v in c.items():
            if v > 1 :
                return i

        