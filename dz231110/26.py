a = []
with open("26.txt","r") as f:
    n = int(f.readline())
    for i in f.readlines():
        a.append(int(i.strip()))
a.sort(reverse=True)
ls = a[0]
s = 1
for i in range(1, n):
    if ls - a[i] >= 3:
        s += 1
        ls = a[i]

print(s)
print(ls)
