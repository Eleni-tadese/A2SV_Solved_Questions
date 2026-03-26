def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    diffs = []
    for i in range(n - 1):
        diffs.append(arr[i+1] - arr[i])

    total = arr[-1] - arr[0]
    diffs.sort(reverse=True)

  
    for i in range(k - 1):
        total -= diffs[i]

    print(total)


solve()
