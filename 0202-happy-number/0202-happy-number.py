class Solution:
    def isHappy(self, n: int) -> bool:
        prev=set()
        while n!=1 and n not in prev:
            prev.add(n) #{19} {19,82}  {19,82,68} {19,82,68,100} 
            n2=str(n) #19
            l=[] #[]
           
            for i in range(len(n2)):
                l.append(n2[i])  #[1,9] [8,2] [6,8] [1,0,0]

            n=0
            for ns in l:
                n += int(ns)**2  #n = 82 n=68 n=100 n=1
        # when n==1 while condition become false 
        return n == 1

# Example when n = 2
    # prev = {2}
# Next:.....
        # prev = {2, 4, 16, 37, 58, 89, 145, 42, 20}
        # 20 -> 4
# Now:
        # n = 4
        # BUT 4 is already in prev
        
        # So:
        # n not in prev  → FALSE
        # while condition breaks
        
        # return n == 1   # returns False


        