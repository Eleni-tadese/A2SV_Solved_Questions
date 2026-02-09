class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=""
        answer =[]
        for numbers in nums:
            s += str(numbers)
        for ch in s:
            answer.append(int(ch))
        return answer