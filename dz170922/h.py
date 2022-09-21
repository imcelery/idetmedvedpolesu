def h(a, b):
    m = (a - 1) // 2
    return b // (a - m)


if __name__ == '__main__':
    n = int(input())
    for j in range(n):
        a, b = list(map(int, input().split(" ")))
        print(h(a, b))