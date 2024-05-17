def f(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    return f(x + 1, y) + f(x * 2, y)
print(f(3, 6) * f(6, 12) * f(12, 16))