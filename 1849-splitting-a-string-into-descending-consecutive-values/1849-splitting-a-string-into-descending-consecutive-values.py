class Solution:
    def splitString(self, s: str) -> bool:
        # check if each lengh one work if not
        # vhevk length to also again

        c = []  

        def back(idx: int) -> bool:
           
            if idx == len(s):
                if len(c) < 2:
                    return False
                for i in range(1, len(c)):
                    if c[i - 1] - c[i] != 1:
                        return False
                return True

           
            for j in range(idx, len(s)):
                val = int(s[idx:j + 1])
                c.append(val)
                if back(j + 1):
                    return True
                c.pop()
            return False

        return back(0)