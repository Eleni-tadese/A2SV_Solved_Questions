class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        m = max(instructions)
        bit = [0] * (m + 1)
        
        def update(i):
            while i <= m:
                bit[i] += 1
                i += i & (-i) 
        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i) 
            return s
        
        total_cost = 0
        MOD = 10**9 + 7
        
        for i, val in enumerate(instructions):   
            less_than = query(val - 1)
            greater_than = i - query(val)
            
            total_cost += min(less_than, greater_than)
            update(val)
            
        return total_cost % MOD