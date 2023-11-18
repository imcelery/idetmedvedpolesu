# from collections import defaultdict
# a = []
# with open("26.txt", "r") as f:
#     n = int(f.readline())
#     for i in range(n):
#         a.append(list(map(int, f.readline().split())))
# a = sorted(a)
# print(a)
# d = defaultdict(lambda : 100000)
# def f(t, m):
#     if d[m] > t:
#         d[m] = t
#         l = m
#         if l == n:
#             return
#         while t > a[l][0]:
#             l += 1
#             if l == n:
#                 return
#         for i in range(l, min(l + 20, n)):
#             f(a[i][1] + 15, m + 1)
# f(0, 0)
# print(d)

# print(bin(int(("120.91.176.213").replace(".",""))))
# print(bin(int(("120.91.174.205").replace(".",""))))
# print(oct(int("101101000010110000101" + "0000000000000", 2)))

print(bin(1111111110))
print(bin(1444444416))
print(1444444416 - 1111111110 - 1)
