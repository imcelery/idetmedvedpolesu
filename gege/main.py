# Доступны файлы для чтения: 27_A.txt, 27_B.txt
a = []
with open("27_A.txt", "r") as f:
    n, k = list(map(int, f.readline().split()))
    d = {}
    for i in range(n):
        x, y = list(map(int, f.readline().split()))
        if x in d.keys():
            d[x] += (y // 2) + (y % 2)
        else:
            d[x] = y // 2 + y % 2

    a = sorted(list(d.keys()))
    b = []
    for i in a:
        b.append(d[i])
    l = 0
    s = 0
    ps = 0
    for i in range(len(a)):
        s += (k - a[i]) * b[i]
        ps += b[i]

    pl = 0
    ti = 0
    mins = s
    k = 0
    for i in range(len(a)):
        while True:
            ns = s - ps + pl
            print(ns)
            if ns < s:
                ps -= b[ti] * (-a[ti] + a[(ti + 1) % len(a)])
                pl += b[ti] * (a[ti] - a[(ti - 1) % len(a)])

                s = ns
                mins = min(mins, s)
                ti = (ti + 1) % len(a)

            else:
                print(ti)
                break

        s += ps - pl
        if a[k] == i:
            pl -= b[k]
            ps += b[k]
            k += 1
        mins = min(mins, s)

    print(mins)
