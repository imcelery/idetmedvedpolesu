o = []
for i in range(2, 40, 2):
    for j in range(1, 40, 2):
        s = pow(2, i) * pow(3, j)
        if 600_000_000 >= s >= 400_000_000:
            o.append(s)
print(sorted(o))
