class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        no_fives=0
        no_tens=0

        for bill in bills:
            if bill ==5:
                no_fives+=1
            elif bill==10:
                if no_fives==0:
                    return False
                no_fives-=1
                no_tens+=1
            else:
                if no_fives >0 and no_tens>0:
                    no_fives-=1
                    no_tens-=1
                elif no_fives>=3:
                    no_fives-=3
                else:
                    return False
        return True