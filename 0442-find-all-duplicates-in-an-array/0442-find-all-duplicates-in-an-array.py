class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        store={}
        ans=[]
        # for i in range(len(nums)):
        #     count = nums.count(nums[i])
        #     store[nums[i]]=count
        for num in nums:
            # Update the count in the dictionary manually
            store[num] = store.get(num, 0) + 1
        
        for  key, value in store.items():
            if value ==2:
                ans.append(key)
        return(ans)

        