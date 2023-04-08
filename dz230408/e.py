#Из того что я (не)понял
#Алгоритм обрятный
#сложность - n * k

def f(n, k, b):
    #нициализируем массив каждого положения
    a = [0 for _ in range(n)]
    #попасть на первый можно одним способом
    a[0] = 1

    for i in b:
        a[i - 1] = -1

    #обновляем для следующих элементов
    for i in range(n - 1):
        if a[i] != -1:
            for j in range(1, k + 1):
                if i + j > len(a) - 1:
                    break
                if a[i + j] != -1:
                    a[i + j] += a[i]


    return a[n-1]

if __name__ == "__main__":
    n = list(map(int, input().split()))
    l = int(input())
    if l != 0:
        b = map(int, input().split())
    else:
        b = []
    print(f(n[0], n[1], b))