def c(n, m):
    c = 0
    for i in range(0, 33):
        for j in range(0, 33):
            if i ** 2 + j == n:
                if j ** 2 + i == m:
                    c += 1
    return c


if __name__ == '__main__':
    n, m = list(map(int, input().split(" ")))
    print(c(n, m))