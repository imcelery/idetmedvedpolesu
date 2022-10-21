import itertools


def binsearch(a: list, el) -> int:
    start = 0
    finish = len(a) - 1
    i = 0
    while start <= finish:
        i = (finish + start) // 2
        if a[i] == el:
            return i
        elif a[i] > el:
            finish = i - 1
        elif a[i] < el:
            start = i + 1
    if a[i] < el:
        return i
    elif i > 0:
        return i - 1
    else:
        return -1


def j(q, t, p, a):
    p.insert(0, 0)
    c = list(itertools.accumulate(p))
    start = 0
    r = 0

    for i in range(t):
        b = a[i] + c[start] + r
        start = binsearch(c, b)
        if start == q:
            start = 0
            print(q)
            r = 0
        else:
            print(q - start)
            r = b - c[start]


if __name__ == '__main__':
    q, t = list(map(int, input().split(" ")))
    p = list(map(int, input().split(" ")))
    a = list(map(int, input().split(" ")))
    j(q, t, p, a)