
def getg(n, d):
    delit = []
    for i in range(1, n // 2 + 1, d):
        if n % i == 0:
            delit.append(i)
    delit.append(n)
    if len(delit) > 3:
        return True
    else:
        return False

def f(d):
    a = 1
    while getg(a, d) == False:
        a += 1
    return a


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        d = int(input())
        print(f(d))
