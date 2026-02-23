class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
      
        l,r= 0,len(skill)-1
        check=skill[l] + skill[r]
        sum=0
        while l<r:
            if skill[l]+skill[r] == check:
                sum+=skill[l]*skill[r]
              
            else:
                return -1
            l+=1
            r-=1
        return sum

        # skill.sort()
        # l,r=0,len(skill)-1
        # check = skill[l]+skill[r]
        # ans=0
        # while l<r:
        #     if skill[l]+skill[r] == check:
        #         ans+=skill[l]*skill[r]
        #     else:
        #         return -1
        #     l+=1
        #     r-=1
        # return ans
