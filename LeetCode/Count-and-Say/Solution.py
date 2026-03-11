1class Solution:
2    def countAndSay(self, n: int) -> str:
3        result = "1"
4        for _ in range(n - 1):
5            current = ""
6            i = 0
7            while i < len(result):
8                count = 1
9                while i + 1 < len(result) and result[i] == result[i + 1]:
10                    i += 1
11                    count += 1
12                current += str(count) + result[i]
13                i += 1
14            result = current
15        return result
16