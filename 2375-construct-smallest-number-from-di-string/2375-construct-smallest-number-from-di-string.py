class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        used = [False] * 10
        result = []

        def backtrack(index, current_str):
          
            if index == n + 1:
                return current_str
            
            for num in range(1, 10):
                if not used[num]:
                  
                    if index == 0: 
                        pass
                    else:
                        last_num = int(current_str[-1])
                        if pattern[index-1] == 'I' and not (num > last_num):
                            continue
                        if pattern[index-1] == 'D' and not (num < last_num):
                            continue
                    
                   
                    used[num] = True
                    res = backtrack(index + 1, current_str + str(num))
                    if res: return res 
                    
                 
                    used[num] = False
            return ""

        return backtrack(0, "")