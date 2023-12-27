import math


import time
a = []
k = []
s = 0
with open("27_B.txt", "r") as f:
    n = int(f.readline())
    for i in f.readlines():
        b = i.split()
        a.append([int(b[0]), math.ceil(int(b[1])/36)])
        k.append([int(b[0]) - s, math.ceil(int(b[1])/36)])
        s = int(b[0])
#1
def f(x):
    o = 0
    for i in a:
        o += abs(i[0] - x) * i[1]
    return o

tim = time.time_ns()

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
print(f"Бинарный : {time.time_ns() - tim}")

#2
tim = time.time_ns()
c = 0
cs = 0
b = 0
bs = 0

for i in range(1, n):
    bs += (a[i][0] - a[0][0]) * a[i][1]
    b += a[i][1]

minx = cs + bs

for i in range(1, n):
    bs -= b * k[i][0]
    b -= k[i][1]
    c += k[i - 1][1]
    cs += c * k[i][0]
    minx = min(minx, cs + bs)
print(f"Линия : {time.time_ns() - tim}")
print(minx)


#3
tim = time.time_ns()
print(min(list(map(lambda x: [f(x[0]), x[0]], a))))
print(f"Квадрат : {time.time_ns() - tim}")

