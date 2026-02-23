class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        start = 0
        last = len(numbers) - 1

        while start < last:

            the_sum = numbers[start] + numbers[last]

            if the_sum == target:
               
                return [start + 1, last + 1]

            elif the_sum > target:
                last -= 1

            else:
                start += 1