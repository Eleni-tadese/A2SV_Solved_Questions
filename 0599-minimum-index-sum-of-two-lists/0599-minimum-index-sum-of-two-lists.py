class Solution(object):
    def findRestaurant(self, list1, list2):

        list1_root = []
        list2_root = []
        big_array = []


      
        if len(list1) > len(list2):
            big_array = list1
            small_array = list2
        else:
            big_array = list2
            small_array = list1


      
        common_elements = []

        for element in small_array:
            if element in big_array:
                common_elements.append(element)



        # store value , index
        for index, value in enumerate(list1):
            list1_root.append([value, index])

        for index, value in enumerate(list2):
            list2_root.append([value, index])

      


        # if only one common
        if len(common_elements) == 1:
            return common_elements


        # find minimum index sum
        min_sum = float('inf')
        result = []


        for word in common_elements:

            index1 = -1
            index2 = -1


            # find index in list1
            for item in list1_root:
                if item[0] == word:
                    index1 = item[1]
                    break


            # find index in list2
            for item in list2_root:
                if item[0] == word:
                    index2 = item[1]
                    break


            total = index1 + index2

            print(word, "sum =", total)


            
            if total < min_sum:
                min_sum = total
                result = [word]

            elif total == min_sum:
                result.append(word)


        return result
