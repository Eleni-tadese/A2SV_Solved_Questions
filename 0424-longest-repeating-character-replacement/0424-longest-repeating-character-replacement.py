class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      
        char_count = {}
        left = 0
        max_length = 0
       
        max_freq = 0
        
        for right in range(len(s)):
            
            char_count[s[right]] = char_count.get(s[right], 0) +                  
            max_freq = max(max_freq, char_count[s[right]])
            window_size = right - left + 1
            
            
            if window_size - max_freq > k:
                char_count[s[left]] -= 1
                left += 1
            else:
                max_length = max(max_length, window_size)
        
        return max_length