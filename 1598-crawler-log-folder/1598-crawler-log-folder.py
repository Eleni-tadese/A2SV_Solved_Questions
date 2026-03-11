class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack =[]

        for ch in logs:
            if ch =="./":
                continue
            if ch == "../":
                if stack:
                    stack.pop()
                    
            else:
                stack.append(ch)
        print(stack)
        return len(stack)

        print(stack)