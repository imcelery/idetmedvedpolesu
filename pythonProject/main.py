#
from datetime import datetime
def f(n):
    a = [0, 1]
    i = 1
    while i != n:
        a.append(a[i-1] + a[i])
        i += 1
    return a[n]

memo = {1: 1, 2: 1}
def fd(n):
    if n not in memo:
        memo[n] = fd(n-1)+fd(n-2)
    return memo[n]



values = [50, 10, 36, 10, 1000, 1000, 1000]

start_time =datetime.now()
for j in range(100000):
    for i in values:
        f(i)
a = datetime.now()  - start_time
start_time = datetime.now()
for j in range(100000):
    for i in values:
        fd(i)
b = datetime.now()  - start_time
print(a, b)

#342717FH

#a = [["o", "q", "z"], ["i","j"], ["a", "b", "c"], []]