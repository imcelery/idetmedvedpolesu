def f(s):
    al = "abcdefghijklmnopqrstuvwxyz"
    a = list(str(s))
    b = []
    i = len(a) - 1
    while i != -1:
        if a[i] == "0" and int(a[i-2]+a[i-1]) >= 10:
            print(al[int(a[i-2]+a[i-1])-1])
            b.append(a[i-2]+a[i-1])
            a[i] = "!"
            a.pop(i - 1)
            a.pop(i - 2)
            i -= 2
        i -= 1
    s = ""
    j = len(b) - 1
    for i in a:
        if i == '!':
            s += al[int(b[j]) - 1]
            j -= 1
        else:
            s += al[int(i) - 1]
    return s

if __name__ == '__main__':
    a = int(input())
    for i in range(a):
        g = input()
        s = input()
        print(f(s))