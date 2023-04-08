#Из того что я (не)понял
#Алгоритм обрятный
#сложность - n * m

def f(n, m):
    #нициализируем массив каждого положения
    a = [[0 for k in range(m + 1)] for _ in range(n + 1)]
    #попасть на первый можно одним способом
    a[0][0] = 1


    #обновляем для следующих элементов
    for i in range(n):
        for j in range(m):
            a[i + 1][j] += a[i][j]
            a[i][j + 1] += a[i][j]

    return str(a[n - 1][m - 1] % (10 ** 6 + 7))

if __name__ == "__main__":
    n = list(map(int, input().split()))

    print(f(n[0], n[1]))