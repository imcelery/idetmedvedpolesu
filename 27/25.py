import math

n = 100000

a = [True for _ in range(n + 1)]
for i in range(2, round(math.sqrt(n))):
    for j in range(2, n // i):
        a[i * j] = False
p = []
for i in range(len(a)):
    if a[i]:
        p.append(i)
p = p[2:]

count = 0

i = 10_000_001
while count < 5:
    t = 0
    n = []
    for j in range(len(p)):
        if i % p[j] == 0:
            t += 1
            if p[j] < 1_000:
                break
            elif t < 3:
                n.append(i // p[j])
            else:
                print(n)
                break





    i += 1