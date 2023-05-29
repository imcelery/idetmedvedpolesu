a = []

with open("17.txt") as f:
    for i in f.readlines():
        a.append(int(i))
m = 0
mm = 0
for i in range(9999):
    for j in range(i + 1, 10000):
        s = abs(a[i] - a[j])
        if s % 80 == 0:
            m += 1
            mm = max(s, mm)
print(m, mm)
