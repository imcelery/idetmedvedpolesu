s = "АЁРТШ"
n = 1
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    if (i1 + i2 + i3 + i4 + i5 == "АЁРЁР"):
                        print(n)
                    print(i1 + i2 + i3 + i4 + i5)
                    n += 1