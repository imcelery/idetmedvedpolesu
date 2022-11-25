
def binsearch(a, el) -> int:
    start = 0
    finish = len(a) - 1
    while start <= finish:
        i = (finish + start) // 2
        d = a[i]

        if d == el:
            return i

        elif d < el:
            start = i + 1
        elif d > el:
            finish = i - 1

    if a[i] < el:
        return i
    else:
        return i - 1

def beaty(l, d):
    a = 0
    for i in range(0, len(l) - 2):
        k = binsearch(l[i:], l[i] + d)
        a += (k - 1) * k // 2


    return a


if __name__ == '__main__':
        a = input().split()
        q, d = int(a[0]), int(a[1])
        z = [int(i) for i in input().split()]
        print(beaty(z, d))

