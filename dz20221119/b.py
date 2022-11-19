

def beaty(l, d):
    a = 0
    for i in range(2, len(l)):
        for j in range(1, i):
            for k in range(j):
                if l[i] - l[k] <= d:
                    a += 1
    return a


def zapros(l, a, d):
    nl = l.copy()
    if a in nl:
        nl.pop(l.index(a))
    else:
        nl.append(a)
        nl.sort()
    print(beaty(nl, d))
    return nl

if __name__ == '__main__':
        a = input().split()
        q, d = int(a[0]), int(a[1])
        z = input().split()
        zz = []
        for i in z:
            zz.append(int(i))

        l = []
        for i in zz:
            l = zapros(l, i, d)


