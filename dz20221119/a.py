def pt(n):
    i = n
    if i == 2:
        return 2
    if i % 2 == 0:
        i += 1
    while True:
        a = True
        for j in range(3, n//2, 2):
            if i % j == 0:
                i += 2
                a = False
                break
        if a:
            return i


def f(d):
    b = pt(d + 1)
    a = b * pt(d + b)
    return a


if __name__ == '__main__':

    n = int(input())
    for i in range(n):
        d = int(input())
        print(f(d))
