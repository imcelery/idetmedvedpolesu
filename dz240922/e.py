a = input()
b = input()
c = input()
if "".join(sorted(c)) == "".join(sorted(a+b)):
    print("YES")
else:
    print("NO")
