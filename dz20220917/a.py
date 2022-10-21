def a(l: list):
    s = l[0] + l[1] + l[2]
    if s % 9 == 0:
        c = s // 9
        bo = True
        for i in range(3):
            if l[i] < c:
                bo = False
                break
        if bo:
            return "YES"
    return "NO"
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        b = list(map(int, input().split(" ")))
        print(a(b))