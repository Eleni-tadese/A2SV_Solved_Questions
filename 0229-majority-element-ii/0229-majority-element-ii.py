class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l=[]
        d=Counter(nums)
        for i,v in d.items():
            if v> (n / 3):
                l.append(i)
        print(l)
        return l
        
        