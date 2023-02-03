
def c(n, s, f):
    d = []
    time = s[0]
    for i in range(n -1):

        b = f[i] - time
        d.append(str(b))
        if f[i] > s[i+ 1]:
            time = f[i]
        else:
            time = s[i+1]
    b = f[len(f) - 1] - time
    d.append(str(b))
    return (" ").join(d)



if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        s = [int(i) for i in input().split()]
        f = [int(i) for i in input().split()]
        print(c(n, s, f))