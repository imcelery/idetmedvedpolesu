import math
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 print(f"{x} {y} {z} {w} {int(not (not y or x) or (not z or w) or not z)}")
# print(109178 // 14)
# print(109178 % 14)
#
# print((3390 * 4 + 109178)// 14)
# print((3390 * 4 + 109178) % 14)


# d = {1 : 1}
# for i in range(2, 2024):
#     if i not in d.keys():
#         d[i] = i * d[i - 1]
# print(d[2023]/d[2020])
# a = []
# b = []
# with open("17.txt", "r") as f:
#     for i in f.readlines():
#         i = i.strip()
#         if i[-1] == "3":
#             a.append(int(i))
#         else:
#             b.append(int(i))
# k = pow(max(a), 2)
# print(len(a))
# print(len(b))
# m = 0
# o = 0
# for i in a:
#     for j in b:
#         s = pow(i, 2) + pow(j, 2)
#         if s >= k:
#             o += 1
#             m = max(m, s)
# print(o)
# print(m)

# def f(n):
#     if n == 6:
#         return 1
#     if n > 6:
#         return 0
#     return f(n * 2) + f(n + 1)
#
# def ff(n):
#     if n == 35:
#         return 1
#     if n > 35:
#         return 0
#     if n == 17:
#         return 0
#     return ff(n * 2) + ff(n + 1)
#
# print(f(1))
# print(ff(10))
# print(f(1) * ff(10))

# def f():
#     glas = ["A", "O"]
#     sog = ["C", "D", "F"]
#     o = 0
#     mo = 0
#
#     with open("24.txt", "r") as f:
#         for i in f.readlines():
#             j = 0
#             while True:
#                 if j == len(i):
#                     return mo
#                 while i[j] in glas:
#                     j += 1
#                     if j == len(i):
#                         return mo
#                 while i[j] in sog and i[j + 1] in glas:
#                     o += 1
#                     j += 2
#                     if j == len(i):
#                         return mo
#                 j+= 1
#                 mo = max(mo, o)
#                 o = 0
# print(f())
#
# a = []
# for j in range(10):
#     if int(f"1{j}21394") % 2023 == 0:
#         a.append(int(f"1{j}21394"))
# for i in range(1000):
#     for j in range(10):
#         if int(f"1{j}2139{i}4") % 2023 == 0:
#             a.append(int(f"1{j}2139{i}4"))
# for i in sorted(a):
#     print(f"{i} {i//2023}")

# a = set()
# with open("26.txt", "r") as f:
#     for i in f.readlines():
#         a.add(int(i))
#
# a = sorted(list(a), reverse=True)
# ma = a[0]
# l = 1
# for i in a[1:]:
#     if ma - i >= 3:
#         ma = i
#         l += 1
# print(l)
# print(ma)

a = []
with open("27_B.txt", "r") as f:
    n = int(f.readline())
    for i in f.readlines():
        b = i.split()
        a.append([int(b[0]), math.ceil(int(b[1])/36)])

def f(x):
    o = 0
    for i in a:
        o += abs(i[0] - x) * i[1]
    return o

l = 0
r = n - 1
while l < r:
    i = (l + r) // 2
    if f(a[i+1][0]) > f(a[i][0]):
        r = i - 1
    else:
        l = i + 1
i = (l + r) // 2
print(f(a[i][0]))
print(a[i][0])
