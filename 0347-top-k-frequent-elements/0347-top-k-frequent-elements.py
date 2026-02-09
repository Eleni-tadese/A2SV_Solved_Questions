class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        data=Counter(nums)
      
        
        apprance = sorted(data.items(), key=lambda item: item[1], reverse=True)
        print(apprance)
        freqent=[]
        for key, value in apprance:
            freqent.append(key) 
        print(freqent)
        return freqent[:k]
     
