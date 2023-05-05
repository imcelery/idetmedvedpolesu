

def f(n, a):
    b = []
    if n == 0:
        return a
    if n >= 6 and not 1 in a and not 5 in a:
        b.append(f(n-6, a + [6]))
    if n >= 5 and not 1 in a:
        b.append(f(n-5, a + [5]))
    if n >= 1:
        b.append(f(n-1, a + [1]))
    if len(b) == 0:
        return -1
    lm = []
    lenm = 1000
    for i in b:
        if i != -1:
            if lenm >= len(i):
                lenm = len(i)
                lm = i.copy()
    if lenm != 1000:
        return lm
    else:
        return -1


if __name__ == "__main__":
    n = list(map(int, input().split()))
    o = f(n[0], [])
    print(len(o))
    print(" ".join(map(str, o)))