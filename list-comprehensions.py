if __name__ == '__main__':
    pair = []
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if (i + j + k) != n:
                    pair.append([i, j, k])
    print(pair)
