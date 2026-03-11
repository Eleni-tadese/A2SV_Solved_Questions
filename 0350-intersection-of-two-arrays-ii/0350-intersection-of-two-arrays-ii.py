class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        l=[]
        common=[]
        count=0
        for element in c2:
            if  element in c2:
                count= min(c1[element],c2[element])
                for i in range(count):
                    common.append(element)
        print(common)
        return common
      
       