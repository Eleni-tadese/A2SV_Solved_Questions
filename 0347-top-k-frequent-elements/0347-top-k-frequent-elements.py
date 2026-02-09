class Solution(object):
    def topKFrequent(self, nums, k):
        numcount=Counter(nums)
        numcount=sorted(numcount.items(),key=lambda x:x[1],reverse=True)
        ans=[]
        for i in range(k):
            pair=numcount[i]
            ans.append(pair[0])
        return (ans)
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        