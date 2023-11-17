import queue
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

k = int(input())
s, fin = list(map(int, input().split()))
fin -= 1
s -= 1
d = [n + 1] * n
d[s] = 0
q = queue.Queue()
q.put(s)
while not q.empty():
    x = q.get()
    l = d[x]
    if x != fin:
        for i in range(n):
            if l + 1 < d[i]:
                if abs(a[x][0] - a[i][0]) + abs(a[x][1] - a[i][1]) <= k:
                    d[i] = l + 1
                    q.put(i)



if d[fin] != n + 1:
    print(d[fin])
else:
    print(-1)
