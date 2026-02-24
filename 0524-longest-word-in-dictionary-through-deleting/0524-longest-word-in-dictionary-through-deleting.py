class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        words=[]
        

        for w in dictionary :
            p1=0
            p2=0
            while p1 < len(s) and p2 < len(w):
                if w[p2] == s[p1]:
                    p1+=1
                    p2+=1
                else:
                    p1+=1
            if  p2 == len(w):
                words.append(w)        
        words.sort(key=lambda x: (-len(x), x))

        if words:
            return words[0]
        else:
            return ""
        