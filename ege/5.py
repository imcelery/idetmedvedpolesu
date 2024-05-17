def f(x):
    if x % 2 == 0:
        return int("1" + bin(x)[2:] + "1", 2)
    else:
        return int(bin(x)[2:] + "10", 2)
for i in range(1000):
    if f(i) > 179:
        print(i)
        break