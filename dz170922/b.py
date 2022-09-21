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
            a, b = b, a + b
            if a == i or b == i:
                s += "O"
            else:
                s += "o"
    return s


if __name__ == '__main__':
    n = int(input())
    print(b(n))