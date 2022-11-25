def f(x, y):
    return x - y

def binsearch(a, el, x) -> int:
    start = 0
    finish = len(a) - 1
    while start <= finish:
        i = (finish + start) // 2
        d = f(a[i], x)

        if d == el:

            return i
        elif d < el:
            start = i + 1
        elif d > el:
            finish = i - 1

    if f(a[i], x) < el:
        return i
    else:
        return i - 1

def beaty(l, d):
    a = 0
    for i in range(0, len(l) - 2):
        k = binsearch(l[i:], d, l[i])
        a += (k - 1) * k // 2


def zapros(l, a, d):
    if a in l:
        l.pop(l.index(a))
    else:
        l.append(a)
        l.sort()
    print(beaty(l, d))
    return l

if __name__ == '__main__':
        a = input().split()
        q, d = int(a[0]), int(a[1])
        z = [int(i) for i in input().split()]

        l = []
        for i in z:
            l = zapros(l, i, d)


