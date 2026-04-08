class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c= Counter(nums)
        arr= sorted(c.items(), key=lambda item: item[1], reverse=True)
        l=[]
        for i in arr:
            l.append(i[0])
        return l[:k]
   