

def obhod(d, s, was):
    if s not in was:
        was.add(s)
        for i in d[s]:
            was.update(obhod(d, i, was))
    return was




if __name__ == '__main__':
    n, s = list(map(int, input().split()))
    d = {}
    for i in range(1, n + 1):
        d.update({i: []})
        a = list(map(int, input().split()))
        for j in range(0, n):
            if a[j] == 1:
                d[i].append(j + 1)
    was = set()

    print(len(obhod(d, s, was)))