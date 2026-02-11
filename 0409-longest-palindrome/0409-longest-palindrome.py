class Solution:
    def longestPalindrome(self, s: str) -> int:
        c=Counter(s)
        print(c)


        l=0
        for letters in c:
            if c[letters]%2==0:
                l+=c[letters]
        # print(set(s))
        if len(s) ==1:
            return 1
        elif len(set(s)) ==1:
            print(l)
            return l
        else:
           return l+1
        