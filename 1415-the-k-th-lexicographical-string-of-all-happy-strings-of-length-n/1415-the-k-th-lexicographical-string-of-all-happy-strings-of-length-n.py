class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # ሁሉንም Happy Strings የምናከማችበት ዝርዝር
        happy_strings = []

        def backtrack(current_path):
            if len(current_path) == n:
                happy_strings.append("".join(current_path))
                return
            if len(happy_strings) == k:
                return
            for char in ["a", "b", "c"]:

                if not current_path or current_path[-1] != char:
                    current_path.append(char)
                    backtrack(current_path)
                    current_path.pop()

        backtrack([])
        return happy_strings[k - 1] if len(happy_strings) >= k else ""
