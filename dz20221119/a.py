
def getg(n, d):
    delit = [1]
    for i in range(1, n // 2 + 1):
        if n % i == 0:

            if len(delit) != 0:
                if i - delit[-1] < d:
                    return False
            delit.append(i)
    delit.append(n)
    if len(delit) > 3:
        return True
    else:
        return False

def f(d):
    a = (1 + d) * (1 + 2 * d)
    while getg(a, d) == False:
        a += d
    return a


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        d = int(input())
        print(f(d))
