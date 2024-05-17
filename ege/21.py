def f(l, x, y = 16):
    if x + y >= 143:
        return l % 2 == 0
    if l == 4:
        return 0
    if l % 2 == 1:
        bo = False
        bo += f(l + 1, x + 3, y)
        bo += f(l + 1, x, y + 3)
        bo += f(l + 1, x * 2, y)
        bo += f(l + 1, x, y * 2)
        return bo
    else:
        bo = True
        bo = bo and f(l + 1, x + 3, y)
        bo = bo and f(l + 1, x, y + 3)
        bo = bo and f(l + 1, x * 2, y)
        bo = bo and f(l + 1, x, y * 2)
        return bo
def f1(l, x, y = 16):
    if x + y >= 143:
        return l == 2
    if l == 2:
        return 0
    if l % 2 == 1:
        bo = False
        bo = bo or f1(l + 1, x + 3, y)
        bo = bo or f1(l + 1, x, y + 3)
        bo = bo or f1(l + 1, x * 2, y)
        bo = bo or f1(l + 1, x, y * 2)
        return bo
    else:
        bo = True
        bo = bo and f1(l + 1, x + 3, y)
        bo = bo and f1(l + 1, x, y + 3)
        bo = bo and f1(l + 1, x * 2, y)
        bo = bo and f1(l + 1, x, y * 2)
        return bo

for i in range(1, 124):
    if f(0, i) and not f1(0, i):
        print(i)