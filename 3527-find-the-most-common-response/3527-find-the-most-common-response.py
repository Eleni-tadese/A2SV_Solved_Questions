class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        l=[]
        for res in responses :
            l.append( list(set(res)))
        counts={}
        for unique_res in l:
            for e in unique_res:
                counts[e] = counts.get(e, 0) + 1
        x=0
        for resp, freq in counts.items(): 
            x=max(x,freq)
        good_response=[]
        for key, value in counts.items():
            if value == x:
                good_response.append(key)
        good_response.sort()  
        print(good_response[0])
        return good_response[0]
      