import math
def b(n, s):
    d = s[0]
    s =s[1:]
    s = sorted(s)
    for i in range(len(s)):
        if(d < s[i]):
            d += math.ceil((s[i] - d)/2)

    return d

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        s =[int(i) for i in input().split()]
        print(b(n, s))