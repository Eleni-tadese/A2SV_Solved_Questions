class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []

        changed.sort()
        exist = Counter(changed)
        original = []

        for value in changed:
            if exist[value] == 0:
                continue  # skip already used numbers

            if value == 0:
                # zeros must be in pairs
                if exist[value] % 2 != 0:
                    return []  # impossible
                original.extend([0] * (exist[value] // 2))
                exist[value] = 0  # mark all zeros used
                continue

            if exist[value*2] == 0:
                return []  # cannot pair, impossible

            # normal pairing
            original.append(value)
            exist[value] -= 1
            exist[value*2] -= 1

        return original
