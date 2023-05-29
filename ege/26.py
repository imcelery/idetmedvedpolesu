def f(name):
    m = {}
    with open(name) as f:
        bo = True
        for i in f.readlines():
            if bo:
                bo = False
                continue
            r, n = map(int, i.split())
            if r in m.keys():
                m[r].append(n)
            else:
                m.update({r:[n]})


    for i in sorted(m.keys(), reverse=True):
        if len(m[i]) > 1:
            d = sorted(m[i])
            for j in range(len(d) - 1):
                if d[j + 1] - d[j] == 14:
                    return i, d[j]
print(f("26.txt"))


