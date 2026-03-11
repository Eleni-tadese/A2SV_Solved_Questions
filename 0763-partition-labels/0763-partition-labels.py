class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index ={}

        for index,character in enumerate(s):
            last_index[character] = index
        print(last_index)
        

        result = []

        size=0
        end=0
        for index, character in enumerate(s):
            size +=1

            if last_index[character] > end:
                end = last_index[character]

            end= max(end,last_index[character])


            if index == end:
                result.append(size)
                size=0
        return result