class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts=Counter(s)
        print(counts)
        # count = sorted( counts, key=lambda item: item[1], reverse=True)
        # print(count)
        maps=[]
        st=0
        for i,v in enumerate(s):
            maps.append([v,i])
        for i in range(len(maps)):

            if counts[ (maps[i][0]) ] ==1 :
                st=maps[i][1]
                break
            else:
                st=-1

        print(maps)
        return st
     
        