class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sums=0
        even=[]

        for v in nums:
                if v%2 == 0:
                    even_sums+=v
        # initial even sum = 6

        for value, index in queries:
           # If current number is even, remove it first , 2
            if nums[index] % 2 == 0:
                even_sums -= nums[index]  #8-2=6 6-2=4
            
            # Update the number 1 is od so become 1+1=2  ,
            nums[index] += value #-1

            # If updated number is even, add it  the udated value 2 is even 
            if nums[index] % 2 == 0:
                even_sums += nums[index]  #6+2 =8
            
            # [2, -1, 3, 4] current array

            even.append(even_sums) #[8] [8,6]
            
            
        return even
        