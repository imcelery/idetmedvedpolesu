
def e(n, a):
    m = 1
    for i in range(n):
        mn = 1
        while a[i] != -1:
            i = a[i] - 1
            mn += 1
        m = max(mn, m)
    print(m)



if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    d = e(n, a)
