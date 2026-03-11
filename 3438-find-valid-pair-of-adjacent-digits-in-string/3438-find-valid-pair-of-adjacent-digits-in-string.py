class Solution:
    def findValidPair(self, s: str) -> str:
        count=Counter(s)
        l=""
        print(s)
        for num , value in count.items():
            if int(num) == value:
                l+=num
        
        print(l)
        if len(l)>1:
            return l
        else:
            return ""
        