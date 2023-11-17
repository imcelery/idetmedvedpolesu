n = int(input())
old = None
for i in range(n):
    a = input()
    if a != old:
        old = a
        print(f"{old}")
