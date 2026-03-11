class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []                
        n = len(arr)

       
        for target_value in range(n, 1, -1):

           
            current_position = arr.index(target_value)

            
            if current_position == target_value - 1:
                continue

            
            if current_position != 0:
                flips.append(current_position + 1)
                arr[:current_position+1] = reversed(arr[:current_position+1])

           
            flips.append(target_value)
            arr[:target_value] = reversed(arr[:target_value])

        return flips