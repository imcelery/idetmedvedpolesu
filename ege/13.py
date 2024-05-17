n = 0
for i1 in range(2):
    for i2 in range(2):
        for i3 in range(2):
            for i4 in range(2):
                for i5 in range(2):
                    for i6 in range(2):
                        if (i1 + i2 + i3 + i4 + i5 + i6) % 3 == 0:
                            n += 1
print(n)