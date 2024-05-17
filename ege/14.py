s = "0123456789abcdefghijklmnopqrs"
for i in s:
    a = int("42" + i + "158", 29) + int("16" + i + "234", 29)
    if a % 28 == 0:
        print(i, a, a / 28)