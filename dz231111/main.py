# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f1 = (w == x) and ( (not y) or (z))
#                 f2 = not(x or (not w)) or (y == z)
#                 print(f"{x} {y} {z} {w} || {int(f1)} {int(f2)}")
#
# print(1555555666 // 16 - 1222222222 // 16)

# from turtle import *
#
# for steps in range(8):
#     forward(80)
#     right(45)
#
# back(200)
#
# for i in range(20):
#     forward(500)
#     right(90)
#     forward(10)
#     right(90)
#     forward(500)
#     left(90)
#     forward(10)
#     left(90)
# left(90)
# for i in range(20):
#     forward(500)
#     right(90)
#     forward(10)
#     right(90)
#     forward(500)
#     left(90)
#     forward(10)
#     left(90)
#
# mainloop()

# s = 0
# for i1 in "аглоь":
#     for i2 in "аглоь":
#         for i3 in "аглоь":
#             for i4 in "аглоь":
#                 for i5 in "аглоь":
#                     s += 1
#                     print(i1 + i2 + i3 + i4 + i5 + " " + str(s))
# print(7 + 3 * pow(37, 2) + 4 * pow(37, 3) + 6 * pow(37, 4) + 2 * pow(37, 6) + 1 * pow(37, 7))
# a = []
# for x in range(37):
#     for y in range(37):
#         if (100074781643 + x * pow(37, 5) + y * 37) % 36 == 0:
#             a.append(y * 37 + x)
# print(a)
# print(max(a))
a = []
mx = 0
with open("17.txt", "r") as f:
    for i in f.readlines():
        b = int(i)
        if b % 100 == 19:
            mx = max(b, mx)
        a.append(b)
ms = 0
c = 0
for i in range(2, len(a)):
    if (a[i - 2] % 3 == 0) or (a[i - 1] % 3 == 0) or (a[i] % 3 == 0):
        if int(a[i - 2] >= 1000) + int(a[i - 1] >= 1000) + int(a[i] >= 1000) == 2:
            sss = a[i - 2] + a[i - 1] + a[i]
            if sss > mx:
                c += 1
                ms = max(ms, sss)
print(c)
print(ms)

# def f(x):
#     if x == 25:
#         return 1
#     if x > 25:
#         return 0
#     if x == 12:
#         return 0
#     return f(x + 1) + f(x * 2) + f(x * x)
# print(f(3))
# ms = 0
# j = 0
# isa = False
# isb = False
# s = ""
# with open("24.txt", "r") as f:
#     for i in f.readlines():
#         s += i
#
# for i in range(len(s)):
#     if s[i] == "A":
#         if not isa:
#             isa = True
#         else:
#             while s[j] != "A":
#                 j += 1
#                 if s[j] == "B":
#                     isb = False
#             j += 1
#
#     if s[i] == "B":
#         if not isb:
#             isb = True
#         else:
#             while s[j] != "B":
#                 j += 1
#                 if s[j] == "A":
#                     isa = False
#             j += 1
#     if isb and isa:
#         ms = max(ms, i - j)
# print(ms)
# aa = []
# for i in range(10):
#     for j in range(10000):
#         a = int(f"3{j}6906{i}4")
#         if a <= pow(10, 10) and a % 2024 == 0:
#             aa.append(a)
# for i in range(10):
#     a = int(f"36906{i}4")
#     if a <= pow(10, 10) and a % 2024 == 0:
#         aa.append(a)
# print(sorted(aa))
# a = []
# q = []
# with open("27-A.txt", "r") as f:
#     n = f.readline()
#     k = f.readline()
#     for i in f.readlines():
#         a.append(i)
#
