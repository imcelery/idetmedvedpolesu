with open("9.csv", "r") as f:
    o = 0
    for i in  f.readlines():
        a = list(map(int, i.split(";")))
        s = sum(a)
        if s % 2 == 0 and max(a) < s - max(a):
            if a[0] + a[1] == a[2] + a[3] or a[0] + a[2] == a[1] + a[3] or a[0] + a[3] == a[1] + a[2]:
                o += 1
print(o)
