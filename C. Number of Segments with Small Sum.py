n, s = map(int, input().split())
a = list(map(int, input().split()))

p1 = 0
current_sum = 0
count = 0

for p2 in range(n):
    current_sum += a[p2]

    while current_sum > s:
        current_sum -= a[p1]
        p1 += 1

    count += (p2 - p1 + 1)

print(count)
