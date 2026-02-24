class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        s=0
        e=len(skill)-1

        intial_sum=skill[s]+skill[e]
        all_sum=0
        
        while s<e:
            if skill[s]+skill[e] == intial_sum:
              all_sum+=skill[s]*skill[e]
              
            else:
                return -1
            s+=1
            e-=1
        return all_sum