class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:


        # mydict = {}
        # for i in range(len(names)):
        #     mydict[names[i]]=heights[i]
        # # print(mydict)
    #    names = ["Mary","John","Emma"], heights = [180,165,170]

        s =len(names)
        for i in range(s):
            for j in range(s-1 ,i, -1):
                if heights[j]>heights[j-1]:
                    heights[j],heights[j-1]=heights[j-1],heights[j]
                    names[j],names[j-1]=names[j-1],names[j]
        return names