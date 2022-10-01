def sort_p(a):
    for i in range(len(a) - 1):
        xi = i
        for j in range(i + 1, len(a)):
            if a[xi] > a[j]:
                a[xi], a[j] = a[j],  a[xi]
    return a

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = {}
    c = []
    for i in range(n):
        if a[i] % 2 == 0:
            b.update({i : a[i]})
        else:
            c.append(a[i])
    c = sort_p(c)
    d = []
    j = 0
    for i in range(n):
        if i in b.keys():
            d.append(b[i])
        else:
            d.append(c[j])
            j += 1
    print(" ".join(list(map(str, d))))

