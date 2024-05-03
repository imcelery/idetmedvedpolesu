#1
import math
#
# with open("27_B_2024.txt") as f:
#     k = int(f.readline())
#     n = int(f.readline())
#     a = list(map(int, f.readlines()))
#     max1, max2, max3 = -10**18, -10**18, -10**18
#     for i in range(2 * k, n):
#         max1 = max(max1, a[i - 2 * k])
#         max2 = max(max2, max1 + a[i - k])
#         max3 = max(max3, max2 + a[i])
#     print(max3)

# with open("27_B.txt") as f:
#     n = int(f.readline())
#     a = []
#     for i in f.readlines():
#         c, b = list(map(int, i.split()))
#         a.append([c, (b + 35) // 36])
#     b = [0] * n
#     ps = 0
#     ls = a[0][0]
#     ds = 0
#     for i in range(n):
#         b[i] = ps * (a[i][0] - ls) + ds
#         ls = a[i][0]
#         ps += a[i][1]
#         ds = b[i]
#
#     c = [0] * n
#     ps = 0
#     ls = a[-1][0]
#     ds = 0
#     for i in range(n - 1, -1, -1):
#         c[i] = ps * (ls - a[i][0]) + ds
#         ls = a[i][0]
#         ps += a[i][1]
#         ds = c[i]
#
#     ms = math.inf
#     for i in range(n):
#         ms = min(ms, c[i] + b[i])
#     print(ms)

with open("27_B.txt") as f:
    n, k = list(map(int, f.readline().split()))
    a = []
    for i in f.readlines():
        c, b = list(map(int, i.split()))
        a.append([c, (b + 1) // 2])
    a.sort()

    r = 0
    ps = 0
    a.append(a[-1])
    s = 0
    for i in range(n - 1, 0, -1):
        s += ps * (a[i + 1][0] - a[i][0])
        ps += a[i][1]
    pt = 0
    while r + 1 != n and s > s - a[r + 1][1] * (a[r + 2][0] - a[r + 1][0]) + a[r + 1][1] * (a[r + 1][0] - a[r][0]):
        r += 1
        s = s - a[r + 1][1] * (a[r + 2][0] - a[r + 1][0]) + a[r + 1][1] * (a[r + 1][0] - a[r][0])
        pt += a[r + 1][1]
    mins = s
    r = 0
    ps += a[0][1]
    for i in range(1, n - 1):
        s += ps * (a[i][0] - a[i - 1][0])
        ps += a[i][1]
        s -= pt * (a[i + 1][0] - a[i][0])
        pt -= a[i + 1][1]
        mins = min(s, mins)
    print(mins)



