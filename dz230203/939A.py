
def a(n, s):
    for i in range(len(s)):
        if s[s[s[i] - 1]-1] - 1 == i:

            return "YES"

    return "NO"


if __name__ == '__main__':
    n = int(input())
    s =[int(i) for i in input().split()]
    print(a(n, s))