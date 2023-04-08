#Из того что я (не)понял
#Алгоритм обрятный
#сложность - n * m

def f(n, m, b):
    #нициализируем массив каждого положения
    a = [[-10_000 for k in range(m + 1)] for _ in range(n + 1)]
    #попасть на первый можно одним способом
    a[0][0] = 0

    #обновляем для следующих элементов
    for i in range(n):
        for j in range(m):
            a[i][j] += b[i][j]
            if a[i][j] > a[i + 1][j]:
                a[i + 1][j] = a[i][j]


            if a[i][j] > a[i][j + 1]:
                a[i][j+1] = a[i][j]
    i = n - 1
    j = m - 1
    s = ""
    for _ in range(i * j):
        if a[i - 1][j] < a[i][j - 1]:
            i -= 1
            s = "D" + s
        else:
            j -= 1
            s = "R" + s
    return a[n - 1][m - 1], s

if __name__ == "__main__":
    n = list(map(int, input().split()))
    b = []
    for i in range(n[0]):
        b.append(list(map(int, input().split())))
    o = f(n[0], n[1], b)
    print(o[0])
    print(o[1])