n = int(input()) * 2

def f(n, x, s):
    if n == 0:
        print(s)
    else:
        if n == x:
            f(n - 1, x - 1, s + ")")
        else:
            f(n - 1, x + 1, s + "(")
            if x:
                f(n - 1, x - 1, s + ")")
f(n, 0, "")