class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str,nums))
        #  print(nums)

        def comparision (num1,num2):
            if num1+num2 > num2+num1:
                return -1
            elif num1+num2 > num2+num1:
                return 1
            else:
                return 0
        nums.sort(key=cmp_to_key(comparision))
        # print(nums) ['9', '5', '34', '3', '30']
        largest_num= "".join(nums)
        if largest_num[0] =="0":
            return "0"
        return (largest_num)

