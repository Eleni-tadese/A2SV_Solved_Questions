from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        total_element=len(nums)
        itemset=Counter(nums)
        for item, number  in itemset.items():
            if number > total_element/2:
                return(item)
        
        