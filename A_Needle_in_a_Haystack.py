t = int(input())
for _ in range(t):
    s = input()
    t = input()
    t_counts = [0] * 26
    for char in t:
        t_counts[ord(char) - ord('a')] += 1
    possible = True
    s_counts = [0] * 26
    for char in s:
        s_counts[ord(char) - ord('a')] += 1

    for i in range(26):
        if t_counts[i] < s_counts[i]:
            possible = False
            break

    if not possible:
        print("Impossible")
        continue

    for i in range(26):
        t_counts[i] -= s_counts[i]

    res = []
    for char in s:
        char_idx = ord(char) - ord('a')

        for i in range(char_idx):
            if t_counts[i] > 0:
                res.append(chr(i + ord('a')) * t_counts[i])
                t_counts[i] = 0

        res.append(char)

    for i in range(26):
        if t_counts[i] > 0:
            res.append(chr(i + ord('a')) * t_counts[i])

    print("".join(res))
