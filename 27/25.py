import math

n = 100000

a = [True for _ in range(n + 1)]
for i in range(2, round(math.sqrt(n))):
    for j in range(2, n // i + 1):
        a[i * j] = False
p = []
for i in range(len(a)):
    if a[i]:
        p.append(i)
p = p[2:]
print(p)
count = 0

i = 10_000_000
f = 15_000_000
a = [True for _ in range(f)]


for k in p[:1000]:
    for j in range(1, f // k):
        a[k * j] = False


z = []
for j in range(i, len(a)):
    if a[j]:
        z.append(j)

for j in range(len(p)):
    if p[j] > 1000:
        p = p[j:]
        break

for j in z:
    t = 0
    n = []

    for k in range(len(p)):
        if j % p[k] == 0:
            t += 1

            if t < 2:
                n.append(i // p[k])
            else:
                print(n)
                break


#
# while count < 5:
#     t = 0
#     n = []
#     for j in range(len(p)):
#         if i % p[j] == 0:
#             t += 1
#             if p[j] < 1_000:
#                 print(p[j])
#                 break
#             elif t < 3:
#                 n.append(i // p[j])
#             else:
#                 print(n)
#                 break
#     i += 2