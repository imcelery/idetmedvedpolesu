def f(a, b, c, n):
    l = []
    for i in range(n//a):

        for j in range((n - i*a)//b):

            for k in range((n - i * a - j*b) // c):
                if n == i * a + j * b + k * c:
                    l.append([i, j, k])
    print(len(l))
    for i in l:
        print(" ".join(i))

if __name__ == '__main__':
    inp = input().split()
    a, b, c, n = int(inp[0]), int(inp[1]), int(inp[2]), int(inp[3])
    f(a, b, c, n)

