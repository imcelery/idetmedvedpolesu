
w = int(input())
for _ in range(w):
    n = int(input())
    a =  []
    b = 0
    for j in range(n * 2 - 1):
        h = list(map(int, input().split(" ")))
        a.append(h + [j + 1])
        b += h[1]

    a.sort(key=lambda i: i[0])
    s1 = a[-1][1]
    s2 = 0
    for i in range(n * 2 - 1):
        if i % 2 == 1:
            s1 += a[i][1]
        if i % 2 == 0:
            s2 += a[i][1]
    if s1 >= b / 2:
        print("YES")
        s = [str(int(a[-1][2]))]
        for i in range(n*2 - 1):
            if i % 2 == 1:
                s.append(str(int(a[i][2])))
        print(" ".join(s))
    elif s2 >= b / 2:
        print("YES")
        s = []
        for i in range(n * 2 - 1):
            if i % 2 == 0:
                s.append(str(int(a[i][2])))
        print(" ".join(s))
    else:
        print("NO")
