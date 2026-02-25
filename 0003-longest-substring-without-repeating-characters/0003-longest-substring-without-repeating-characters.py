class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()
        longest = 1
        left = 0

        for i in range(len(s)):

            while s[i] in window:

                window.remove(s[left])
                left+=1

            window.add(s[i])

            longest =max(longest,len(window))

            # i -left +1
        return longest




        