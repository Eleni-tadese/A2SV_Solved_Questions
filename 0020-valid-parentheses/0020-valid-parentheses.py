class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapp = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for braces in s:
            if braces not in mapp.keys():
                stack.append(braces)
            else:
                if not stack:
                    return False

                top = stack.pop()

                if mapp[braces] != top:
                    return False

        return not stack