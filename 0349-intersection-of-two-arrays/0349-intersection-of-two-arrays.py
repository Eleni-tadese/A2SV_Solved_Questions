class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        return list(s1.intersection(s2))
#         Time Complexity: O(n + m)

# set(nums1) takes O(n) time

# set(nums2) takes O(m) time

# s1.intersection(s2) takes O(min(n, m)) on average*

# Total: O(n + m)

# Space Complexity: O(n + m)

# s1 uses O(n) space

# s2 uses O(m) space

# Result uses O(min(n, m)) space

# Total: O(n + m)

        # l3=[]
        # for elements in nums1:
        #     if elements in nums2 :
        #         l3.append(elements)
        # return list(set(l3))

# Time Complexity Analysis
# Let n = len(nums1) and m = len(nums2)

# elements in nums2 is O(m) for each check (linear search through nums2)

# You do this check n times (for each element in nums1)

# Total: O(n × m) → O(n²) in worst case when n ≈ m

# For example: If both arrays have 1000 elements, you're doing ~1,000,000 operations.

# Space Complexity
# O(min(n, m)) for the result list (worst case all elements intersect)

# O(min(n, m)) for the set conversion

# Total: O(min(n, m))


       
        