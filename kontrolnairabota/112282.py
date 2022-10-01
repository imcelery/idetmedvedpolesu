import random

if __name__ == '__main__':
    a, b, n   = list(map(int, input().split()))
    c = [random.randint(a, b) for i in range(n)]
    print(" ".join(list(map(str, c))))
    d = sum(c) / n
    d = "{:.3f}".format(d)
    print(d)

