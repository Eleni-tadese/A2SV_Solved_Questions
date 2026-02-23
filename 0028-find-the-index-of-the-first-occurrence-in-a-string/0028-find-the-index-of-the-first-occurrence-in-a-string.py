class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack ==needle:
            return 0
        for i in range(len(haystack)-len(needle)):
            h = i
            n = 0
            while  n<len(needle) and haystack[h] == needle[n]:
                h+=1
                n+=1
            if n == len(needle):
                    return i
            
        return -1

            