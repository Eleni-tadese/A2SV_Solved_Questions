class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        l=[]
        common=[]
      
        for element in nums1 :
            if element in nums1 and element in nums2:
                common.append(element)
        print(common)
        return common
      
            
        