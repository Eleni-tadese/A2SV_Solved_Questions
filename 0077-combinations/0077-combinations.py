class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
       
        arr = [i for i in range(1, n+1)]
        result = []
        
        def backtrack(index, combination):
        
            if len(combination) == k:
                result.append(combination[:])
                return
            
           
            if index == len(arr):
                return
            
          
            combination.append(arr[index])
            backtrack(index + 1, combination)
            combination.pop() 
            
         
            backtrack(index + 1, combination)
        
        backtrack(0, [])
        return result

