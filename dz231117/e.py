from collections import defaultdict
j = input()
s = input()
dj = defaultdict(int)
ds = defaultdict(int)

for i in j:
    dj[i] += 1

for i in s:
    ds[i] += 1
o = 0


print(int(dj == ds))