n = int(input())
s = 0
ms = 0
for i in range(n):
    a = int(input())
    if a:
        s += 1
    else:
        ms = max(ms, s)
        s = 0
ms = max(ms, s)
print(ms)