def f(n):
    a = [1, 1]
    for i in range(2, n):
        a.append(a[-1] + a [-2])
    return a[n - 1]
if __name__ == '__main__':
    b = int(input())
    a = f(b)
    print(a)

