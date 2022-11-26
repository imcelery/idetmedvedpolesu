def f(x, y):
    if x <= 1 and y >= 1-x:
        if y > 2:
            if y >= 2 * x * x:
                return "YES"
        else:
            return "YES"
    else:
        return "NO"





if __name__ == '__main__':
    inp = input().split()
    a, b = float(inp[0]), float(inp[1])
    print(f(a, b))

