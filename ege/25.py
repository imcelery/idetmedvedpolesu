a = []
for i in range(1000):
    for j in range(10):
        if int(f"10{i}2024{j}") % 2024 == 0:
            a.append(int(f"10{i}2024{j}"))
        x = str(i)
        while len(x) < 3:
            x = "0" + x
        if int(f"10{x}2024{j}") % 2024 == 0:
            a.append(int(f"10{x}2024{j}"))
a.sort()
ls = 0
for i in a:
    if ls != i:
        print(i, i//2024)
    ls = i







