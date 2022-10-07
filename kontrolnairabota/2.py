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
        if i != 0 and i != len(a) - 1:
            if el - a[i] < a[i+1] - el:
                return i
            else:
                return i + 1
        else:
            return i
    elif a[i] > el:
        if i != 0 and i != len(a) - 1:
            if a[i] - el < el - a[i - 1]:
                return i
            else:
                return i - 1
        else:
            return i


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    d = []
    c = []
    for i in range(len(a)):
        if a[i] not in d:
            d.append(a[i])
    for i in b:
        print(d[binsearch(d, i)])