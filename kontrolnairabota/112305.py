if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    c = []
    b = []
    d = 0
    for i in range(n):
        if a[i] == 0:
            d += 1
        elif a[i] not in b:
            b.append(a[i])
            c.append(a[i])
        else:
            d += 1
    for i in range(d):
        c.append(0)
    print(" ".join(list(map(str, c))))
