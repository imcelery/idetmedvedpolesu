
def f(n ,m):
    a = [0, 1, 1, 0]
    c = True
    for i in range(n // 2):
        s1 = ""
        s2 = ""
        for j in range(m//2):
            if c:
                s1 += str(a[0]) + " " + str(a[1]) + " "
                s2 += str(a[2]) + " " + str(a[3]) + " "
            else:
                s1 += str(a[2]) + " " + str(a[3]) + " "
                s2 += str(a[0]) + " " + str(a[1]) + " "

            c = not c
        print(s1)
        print(s2)
        if( m //2 )% 2 == 0:
            c = not c




if __name__ == '__main__':
        a = int(input())
        for i in range(a):
            a = input().split()
            n, m = int(a[0]), int(a[1])
            f(n, m)

