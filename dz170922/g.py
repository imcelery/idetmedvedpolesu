def g(d):
    b = {}
    for i in d:
        if i[0] in b.keys():
            b[i[0]] += i[1]
        else:
            b.update({i[0]: i[1]})
    m = max(b.values())
    b = {k: 0 for k, v in b.items() if v == m}
    for i in d:
        if i[0] in b.keys():
            b[i[0]] += i[1]
            if b[i[0]] >= m:
                return i[0]
if __name__ == '__main__':
    n = int(input())
    d = []
    for j in range(n):
        a, b = input().split(" ")
        d.append((a, int(b)))
    print(g(d))