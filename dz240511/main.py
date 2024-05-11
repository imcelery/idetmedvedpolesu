# for x in range(2):
#     for y in range(2):
#         for u in range(2):
#             for w in range(2):
#                 f = (not( (y <= w) == x)) and u
#                 print(x, y, u, w, int(f))

def c(x, base):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    result = ''
    while x > 0:
        result = digits[x % base] + result
        x //= base
    return result


# def f(x):
#     if x % 7 == 0:
#         x7 = c(x, 7)
#         x7 = x7 + x7[-2:]
#         return int(x7, 7)
#     else:
#         x7 = c(x, 7) + c((x % 7) * 2, 7)
#         return int(x7, 7)
# mx = 0
# for i in range(10, 1000):
#     a = f(i)
#     print(a)
#     if a < 220:
#         mx = i
# print(mx)

# def f(s):
#     while "8858" in s or "555" in s:
#         if "8858" in s:
#             s = s.replace("8858", "4")
#         else:
#             s = s.replace("555", "58")
#
#         if "5858" in s:
#             s = s.replace("5858", "85")
#
#     return sum(map(int, list(s)))
# mx = 0
# for i in range(3, 10001):
#     s = "8" + "5" * i
#     if f(s) == 66:
#         print(i)
#         mx = i
# print(mx)
# s = 0
# for i in range(128):
#     a = bin(i)[2:]
#     a = "0" * (8 - len(a)) + a
#     if a == a[::-1]:
#         s += 1
#         print(a)
# print(s)
# a = 7 * pow(49, 120) - 6 * pow(343, 65) - 5 * pow(7, 40)
# a = c(a, 7)
# s = 0
# for i in a:
#     if i == "6":
#         s += 1
#
# print(a, s)
# from functools import cache
# @cache
# def f(x):
#     if x <= 1:
#         return 1
#     if x % 3 == 0:
#         return f(x - 1) + x // 3
#     else:
#         return f(x - 1) + f(x - 2)
# print(f(54) - f(52) - f(50))

# with open("17.txt", "r") as f:
#     a = []
#     for i in f.readlines():
#         a.append(int(i))
#     m = sorted(a)[-3]
#     print(m)
#     s = 0
#     mx = 0
#     for i in range(len(a) - 2):
#         b = a[i] % 2 + a[i + 1] % 2 + a[i + 2] % 2
#         if b > 0:
#             if a[i] + a[i + 1] + a[i + 2] <= m:
#                 s += 1
#                 mx = max(mx,  a[i] + a[i + 1] + a[i + 2])
#     print(s, mx)

# def f(x, y, h):
#     if x + y >= 150:
#         return h % 2 == 0
#     if h == 0:
#         return False
#
#     a = [f(x + 2, y, h - 1), f(x * 3, y, h - 1), f(x, y + 2, h - 1), f(x, y * 3, h - 1)]
#     if h % 2 == 1:
#         return any(a)
#     else:
#         return all(a)
# for i in range(134):
#     if f(16, i, 4) and not(f(16, i, 2)):
#         print(i)

# def f(x, y, z = -1):
#     if x == z:
#         return 0
#     if x > y:
#         return 0
#     if x == y:
#         return 1
#     return f(x + 1, y, z) + f(x + 4, y, z) + f(x * 3, y, z)
# print(f(7, 27, 11) * f(27, 42))
# with open("24.txt", "r") as f:
#     s = f.readline()
#     mx = 0
#     l = 0
#     for i in range(len(s)):
#         if l >= 4:
#             if s[i - 4:i + 1] == "AHAHA":
#                 mx = max(mx, l)
#                 l = 4
#             else:
#                 l += 1
#         else:
#             l += 1
#     mx = max(mx, l)
#     print(mx)

# for i in range(397438, 443520 + 1):
#     s = 0
#     for j in range(2, int(i ** 0.5)):
#         if i % j == 0:
#             if j % 2 == 0:
#                 s += 1
#             if (i // j) % 2 == 0:
#                 s += 1
#     if s >= 142:
#         print(i, s)
# import codecs
# with codecs.open("Новая таблица - Водители.txt", "r", "utf_8_sig") as f:
#     s = set()
#     for i in f.readlines():
#         a = i.split(",")
#         if a[5].strip() == "Чехов":
#             s.add(a[0])
#     print(s)
from collections import defaultdict
#
# with codecs.open("Новая таблица - Поездки.txt", "r", "utf_8_sig") as f:
#     ss = defaultdict(int)
#     for i in f.readlines():
#         a = i.split(",")
#         if a[1] in s:
#             ss[a[2]] += 1
#     print(ss)
#
# with codecs.open("Новая таблица - Автомобили.txt", "r", "utf_8_sig") as f:
#     d =defaultdict(int)
#     for i in f.readlines():
#         a = i.split(",")
#         if a[0] in ss.keys():
#             d[a[2]] += ss[a[0]]
#     print(d)

# from turtle import *
#
# speed(213213213)
# right(135)
# for i in range(7):
#     forward(7 * 40)
#     right(45)
#     forward(8 * 40)
#     right(135)
#
# penup()
# for x in range(-20, 20):
#     for y in range(-10, 10):
#         setpos(x*40, y*40)
#         dot(4, 'red')
# s = 0
# with open("9.txt", "r") as f:
#     for i in f.readlines():
#         d = defaultdict(int)
#         a = list(map(int, i.strip().split(";")))
#         if sum(a) < 502:
#             for j in a:
#                 d[j] += 1
#             if len(d.keys()) == 5:
#                 if 3 in d.values():
#                     s += 1
#                     print(a)
# print(s)

# for a in range(1000):
#     bo = True
#     for x in range(500):
#         for y in range(500):
#             bo = bo and (((x >= a) or (121 >= x * x)) and ((y * y < 49) or (a < y)))
#     if bo:
#         print(a)

# with open("27_B.txt", "r") as f:
#
#     k, n = list(map(int, f.readline().split()))
#     dp = [10000000000] * n
#     dp[0] = 0
#     for i in range(n):
#         a = int(f.readline())
#         for j in range(1, k + 1):
#             if j + i < n:
#                 dp[j + i] = min(dp[j + i], dp[i] + a)
#     print(dp[n - 1])

with open("26.txt", "r") as f:
    n = int(f.readline())
    d = defaultdict(int)
    a = defaultdict(int)
    b = []
    us = [1] * n
    for i in range(n):
        x, y = list(map(int, f.readline().split()))
        d[x] = i
        d[y] = i
        a[x] = 1
        a[y] = 0
        b.append(x)
        b.append(y)
    b.sort()
    ls = 0
    shlifdo = 0
    shlif = 0
    for i in b:
        if a[i]:
            if us[d[i]] == 1:
                us[d[i]] = 0
                ls = d[i]
                shlifdo = shlif
                shlif += 1
        else:
            if us[d[i]] == 1:
                us[d[i]] = 0
                ls = d[i]
                shlifdo = shlif
    print(ls + 1, shlifdo)
