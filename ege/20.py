def f(l, x, y = 16):
    if x + y >= 143:
        return l == 3
    if l == 3:
        return 0
    if l % 2 == 0:
        bo = False
        bo = bo or f(l + 1, x + 3, y)
        bo = bo or f(l + 1, x, y + 3)
        bo = bo or f(l + 1, x * 2, y)
        bo = bo or f(l + 1, x, y * 2)
        return bo
    else:
        bo = True
        bo = bo and f(l + 1, x + 3, y)
        bo = bo and f(l + 1, x, y + 3)
        bo = bo and f(l + 1, x * 2, y)
        bo = bo and f(l + 1, x, y * 2)
        return bo

for i in range(124):
    if f(0, i):
        print(i)