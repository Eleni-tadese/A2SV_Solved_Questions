class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window =set()
        l=0
        r=0
        longest=0
        while l<len(s) and r<len(s):
            if s[r] in window:
                window.remove(s[l])
                l+=1
                
            else:
                window.add(s[r])
                r+=1

                longest=max(longest,len(window))
                
     
        return longest


        