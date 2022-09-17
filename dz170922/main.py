

def b(n):
    a = 1
    b = 1
    s = ""
    for i in range(1, n + 1):
        if i <= b:
            if a == i or b == i:
                s += "O"
            else:
                s += "o"
        else:
            a, b = b, a+b
            if a == i or b == i:
                s += "O"
            else:
                s += "o"
    return s
def c(n, m):
    c = 0
    for i in range(0, 33):
        for j in range(0, 33):
            if i**2 + j == n:
                if j**2 + i == m:
                    c += 1
    return c


def d(n, a, b):
    a = a + b
    a = list(set(a))
    if len(a) == n:
            return "I become the guy."
    return "Oh, my keyboard!"




def a(l: list):
    s = l[0] + l[1] + l[2]
    if s % 9 == 0:
        c = s // 9
        bo = True
        for i in range(3):
            if l[i] < c:
                bo = False
                break
        if bo:
            return "YES"
    return "NO"
def j(q, t, p, a):
    last = p.copy()
    start = 0
    for i in range(t):
        for j in range(start, len(last)):
            if last[j] <= a[i]:
                a[i] -= last[j]
                start += 1
            else:
                last[j] -= a[i]
                print(len(last) - start)
                break
        if start == len(last):
            print(q)
            last = p.copy()
            start = 0

def g(a, b):
    f = ""
    c = []
    for i in a[::-1]:
        if i not in c:
            f = i
            c.append(i)
    return f

def f(a, k):
    s = 0
    while len(a) > 0:
        if k >= a[0]:
            s += 1
            a.pop(0)
        elif k >= a[-1]:
            s += 1
            a.pop(-1)
        else:
            return s
    return s
if __name__ == '__main__':
    n, k = list(map(int, input().split(" ")))
    a = list(map(int, input().split(" ")))

    print(f(a, k))
