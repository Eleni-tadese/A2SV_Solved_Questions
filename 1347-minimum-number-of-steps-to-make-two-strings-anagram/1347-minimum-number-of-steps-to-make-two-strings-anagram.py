class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1=Counter(s)
        c2 = Counter(t)
        print(c1)
        print(c2)
        print((c1-c2).items())
        print((c1-c2).values())
        min_step = sum((c1-c2).values())
        return min_step
        
