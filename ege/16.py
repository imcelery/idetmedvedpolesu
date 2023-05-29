def f(x):
    if x <= 1:
        return 0
    if x % 2 == 1:
        return f(x - 1) + 3 * x * x
    return x//2 + f(x - 1) + 2
print(f(49))