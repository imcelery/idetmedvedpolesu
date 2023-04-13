#Из того что я (не)понял
#Алгоритм обрятный
#сложность - n * m

def f(n, m):
    #нициализируем массив каждого положения
    a = [[0 for _ in range(m)] for _ in range(n)]
    w = [[True for _ in range(m)] for _ in range(n)]
    #попасть на первый можно одним способом
    a[0][0] = 1

    q = [(0, 0)]

    while len(q) != 0:
        p = q.pop(0)
        if w[p[0]][p[1]]:
            if p[1] + 2 < m and p[0] + 1 < n:

                q.append((p[0] + 1, p[1] + 2))
                a[p[0] + 1][p[1] + 2] += a[p[0]][p[1]]

            if p[1] + 1 < m and p[0] + 2 < n:

                q.append((p[0] + 2, p[1] + 1))

                a[p[0] + 2][p[1] + 1] += a[p[0]][p[1]]
        w[p[0]][p[1]] = False


    return a[n-1][m-1]

if __name__ == "__main__":
    n = list(map(int, input().split()))

    print(f(n[0], n[1]))