def f(x, y):
    if y >= x:
        return ((1 + x) * x + (3 * x - 1 - y) * (y - x)) // 2
    else:
        return ((1 + y) * y) // 2


def binsearch(a, el, x) -> int:
    start = 1
    finish = a
    i = 0
    while start <= finish:
        i = (finish + start + 1) // 2
        d = f(x, i)

        if d == el:
            return i
        elif d > el:
            finish = i - 1
        elif d < el:
            start = i + 1
    if f(x, i) < el:
        if i < a:
            return i + 1
        else:
            return i
    else:
        return i


if __name__ == '__main__':
    n = int(input())
    for j in range(n):
        k, x = list(map(int, input().split(" ")))
        a = binsearch(k * 2 - 1, x, k)
        print(a)