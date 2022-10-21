a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))
b.sort()
c = b[a[2]] - b[a[2] - 1]
print(c)