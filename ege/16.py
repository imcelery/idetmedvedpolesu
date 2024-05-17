import sys
sys.setrecursionlimit(3000)
def f(x):
    if x <= 12:
        return 1
    return f(x - 1) + x - 2
print(f(2024) - f(2020))