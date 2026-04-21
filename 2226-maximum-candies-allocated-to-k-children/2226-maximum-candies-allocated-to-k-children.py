class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
      
        low = 1
        high = max(candies)
        ans = 0
        while low <= high:
            mid = (low + high) // 2

            total_children = 0
            for c in candies:

                total_children += c // mid

            if total_children >= k:

                ans = mid
                low = mid + 1
            else:

                high = mid - 1

        return ans
