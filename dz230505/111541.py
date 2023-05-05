import collections

def obhod(d, s, was):
    if s not in was:
        was.add(s)
        for i in d[s]:
            was.update(obhod(d, i, was))
    return was


def f():
    n = int(input())

    c = 0
    d = collections.defaultdict(list)
    for i in range(1, n + 1):
        d.update({i: []})
        a = list(map(int, input().split()))
        c += sum(a)
        for j in range(0, n):
            if a[j] == 1:
                d[i].append(j + 1)

    if len(obhod(d, 1, set())) == n and (c // 2) + 1 == n:
        print("YES")
    else:
        print("NO")


a = f()