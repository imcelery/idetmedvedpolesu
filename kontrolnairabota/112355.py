if __name__ == '__main__':
    a = input()
    b = []
    d = {"I": 1, "V":5, "X":10, "L": 50, "C": 100,"D" : 500, "M": 1000}
    for i in a:
        b.append(d[i])
    a = 0
    for i in range(len(b)):
        if i + 1 <= len(b) - 1:
            if b[i] < b[i + 1]:
                a -= b[i]
            else:
                a += b[i]
        else:
            a += b[i]
    print(a)
