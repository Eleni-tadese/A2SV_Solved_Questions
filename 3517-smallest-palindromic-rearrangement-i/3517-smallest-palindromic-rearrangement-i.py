from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
       
        count = Counter(s)
        print(count)
        
        first_half = []
        middle = ""
        
      
        for char in sorted(count.keys()):
            freq = count[char]

            print(freq)
            
            if freq % 2 == 1: # odd -this character must be in the middle
                 
               
                if not middle:
                    middle = char
               
                first_half.append(char * (freq // 2))
                
            else: # Even frequency - all go to first half
                first_half.append(char * (freq // 2))
        
        first_half = "".join(first_half)
        
       
        return first_half + middle + first_half[::-1]