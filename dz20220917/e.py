import string


def e(s, p):
    s = list(s)
    b = dict(zip(string.ascii_lowercase, range(1, 27)))
    a = 0
    for j in s:
        a += b[j]
    p = a - p
    b = string.ascii_lowercase
    for i in range(len(b) - 1, -1, -1):
        if p <= 0:
            break
        for j in range(len(s) - 1, -1, -1):
            if s[j] == b[i]:
                s.pop(j)
                p -= i + 1
            if p <= 0:
                break
    return "".join(s)


if __name__ == '__main__':
    n = int(input())
    for j in range(n):
        a = input()
        b = int(input())
        print(e(a, b))