def f(x, y):
    i = 1
    if x < y:
        x, y = y, x
    while x % y != 0:
        y = x % y
        i += 1
    print(y, i)





if __name__ == '__main__':
    inp = input().split()
    a, b = int(inp[0]), int(inp[1])
    f(a, b)




