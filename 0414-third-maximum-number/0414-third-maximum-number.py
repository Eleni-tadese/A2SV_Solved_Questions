class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n=list(set(nums))
        n.sort(reverse=True)
        print(n)

        if len(n) < 3:
            return n[0]
        else:
            return n[2]