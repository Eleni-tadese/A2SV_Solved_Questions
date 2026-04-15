class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
    
        for i in range(1, n):
            for j in range(i + 1, n):
                s1, s2 = num[:i], num[i:j]
                
                if (len(s1) > 1 and s1[0] == '0') or (len(s2) > 1 and s2[0] == '0'):
                    continue
                if self.isValid(s1, s2, j, num):
                    return True
        return False
    def isValid(self, s1, s2, start, num):
        if start == len(num):
            return True
        
        sum_str = str(int(s1) + int(s2))
        
        if not num.startswith(sum_str, start):
            return False
        return self.isValid(s2, sum_str, start + len(sum_str), num)