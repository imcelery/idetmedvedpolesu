import math

n = int(input())
d = {}
for i in range(n):
    a = list(map(int, input().split()))
    d.update({i:{}})
    for j in range(len(a)):
        if a[j] != 0:
            d[i].update({j : a[j]})

def diic(d, n):
    was = set()
    rass = dict.fromkeys(d.keys(), math.inf)
    put = dict.fromkeys(d.keys(), [n])
    rass[n] = 0

    q = [(0, n)]
    while len(q) > 0:
        q.sort()
        a = q.pop(0)
        if a[1] not in was:
            was.add(a[1])
            for i in d[a[1]].keys():
                if d[a[1]][i] != 0:
                    if rass[a[1]] + d[a[1]][i] < rass[i]:
                        rass[i] = rass[a[1]] + d[a[1]][i]
                        put[i] = put[a[1]] + [i]
                    q.append([rass[i], i])
    return rass, put

for i in range(n - 1):
    r, p = diic(d, i)

    for j in r.keys():
        if i < j:
            if r[j] == math.inf or r[j] == 0:
                print(f"({i + 1},{j + 1}): 0")
            else:
                print(f"({i + 1},{j + 1}): " + " ".join(map(lambda x: str(x + 1), p[j])) + f" ({r[j]})")
