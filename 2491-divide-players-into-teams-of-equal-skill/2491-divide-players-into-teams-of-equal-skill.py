class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        s1 = 0
        s2 = len(skill)-1

       
        total=0
        pair=[]

        while s1<s2:
            sums=skill[s1] + skill[s2]
            muls=skill[s1] * skill[s2]
            total+=muls
            pair.append(sums)
        
            s1+=1
            s2-=1

        if len(set(pair))==1:
            return total
        else:
            return -1


        