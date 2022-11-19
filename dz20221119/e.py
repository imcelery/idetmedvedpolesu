def f(x, y):
    return x - y

def binsearch(a, el, x) -> int:
    start = 0
    finish = len(a) - 1
    while start <= finish:
        i = (finish + start) // 2
        d = f(x, a[i])

        if d == el:
            return i
        elif d > el:
            start = i + 1
        elif d < el:
            finish = i - 1
    if f(x, a[i]) > el:
        if i < len(a):
            return i + 1
        else:
            return i
    else:
        return i


def beaty(l, d):
    a = 0
    for i in range(2, len(l)):
        k = binsearch(l[:i], d, l[i])

        a += (i - k - 1) * (i - k) // 2

    return a


if __name__ == '__main__':
        a = input().split()
        q, d = int(a[0]), int(a[1])
        z = [int(i) for i in input().split()]
        print(beaty(z, d))

