class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        child = [0] * k
        self.minunfairness = float('inf') 

        def back(idx: int):
            if idx == len(cookies):
                self.minunfairness = min(self.minunfairness, max(child))
                return

            for i in range(k):
                child[i] += cookies[idx]
                back(idx + 1)
                child[i] -= cookies[idx]

                if child[i] == 0:
                    break

        back(0)
        return self.minunfairness
