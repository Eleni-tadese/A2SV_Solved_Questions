class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        
        
        def count_at_most(max_distinct: int) -> int:
            if max_distinct == 0:
                return 0
            
            freq = Counter()   
            left = 0
            total_subarrays = 0
            
            for right in range(len(nums)):
               
                freq[nums[right]] += 1
                
               
                while len(freq) > max_distinct:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1
                
              
                total_subarrays += (right - left + 1)
            
            return total_subarrays
        
     
        return count_at_most(k) - count_at_most(k - 1)