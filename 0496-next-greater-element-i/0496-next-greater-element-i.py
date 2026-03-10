class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack =[]
        map_dict = defaultdict()
        res=[]

        for num in nums2:
            while stack and stack[-1] <num:
                map_dict[stack.pop()] =num
            stack.append(num)
        for num in stack:
             map_dict[num]=-1
        for num in nums1:
            res.append( map_dict [num])
        return res



            


          

        