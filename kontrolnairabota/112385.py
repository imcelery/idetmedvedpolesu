if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    a = []
    c = []
    for i in range(n):
        b = list(map(int, input().split()))
        c.append(sum(b))
        a.append(b)
    c = sum(c) / n / k
    print("{:.4f}".format(c))
    for i in range(n):
        d = []
        for j in range(k):
            if a[i][j] > c:
                d.append(255)
            else:
                d.append(0)
        print(" ".join(list(map(str, d))))


