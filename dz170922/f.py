def f(a, k):
    s = 0
    while len(a) > 0:
        if k >= a[0]:
            s += 1
            a.pop(0)
        elif k >= a[-1]:
            s += 1
            a.pop(-1)
        else:
            return s
    return s


if __name__ == '__main__':
    n, k = list(map(int, input().split(" ")))
    a = list(map(int, input().split(" ")))

    print(f(a, k))