class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        def dfs(index, prev, count):
            # if used whole string
            if index == n:
                return count >= 2   # need at least 2 numbers

            current = 0

            # try every possible next substring
            for j in range(index, n):
                digit = int(s[j])
                current = current * 10 + digit

                # first number: always allowed
                if prev == -1:
                    if dfs(j + 1, current, count + 1):
                        return True

                # next number must be prev - 1
                elif current == prev - 1:
                    if dfs(j + 1, current, count + 1):
                        return True

                # pruning: too large already
                elif current >= prev:
                    break

            return False

        return dfs(0, -1, 0)