from collections import defaultdict
j = input()
s = input()
dj = {}
ds = defaultdict(int)

for i in j:
    dj[i] = 1

for i in s:
    ds[i] += 1
o = 0

for i in dj.keys():
    o += ds[i]

print(o)