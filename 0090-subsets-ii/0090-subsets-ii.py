class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        nums.sort()
        
        def backtrack(start_index, path): #backtrack(0, []) , (1, [1]) , (2, [1, 2]) , backtrack(3, [1, 2, 2])
            
            res.append(list(path)) #[] [1] [1, 2] [1, 2, 2]
            
            for i in range(start_index, len(nums)):
                if i > start_index and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])  #path = [1] [1, 2] [1, 2, 2]
                backtrack(i + 1, path)
                
                path.pop()
        
        backtrack(0, [])
        return res