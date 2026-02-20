class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []                 # stores the flip sizes we perform
        n = len(arr)

        # We place numbers from biggest to smallest
        for target_value in range(n, 1, -1):

            # Find where this number currently is
            current_position = arr.index(target_value)

            # If it's already at correct position, do nothing
            if current_position == target_value - 1:
                continue

            # If it's not at front, bring it to front first
            if current_position != 0:
                flips.append(current_position + 1)
                arr[:current_position+1] = reversed(arr[:current_position+1])

            # Now move it to its correct position
            flips.append(target_value)
            arr[:target_value] = reversed(arr[:target_value])

        return flips