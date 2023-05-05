#Из того что я (не)понял
#Алгоритм обрятный
#сложность - n * k

def f(n, k, b):
    a = [[-10_001, []] for _ in range(n)]
    a[0][0] = 0
    a[0][1].append(0)

    #обновляем для следующих элементов
    for i in range(n - 1):
        if i != 0:
            a[i][1].append(i)
            a[i][0] += b[i - 1]
        for j in range(1, k + 1):
                if i + j > len(a) - 1:
                    break
                if a[i][0] > a[i + j][0]:
                    a[i + j][0] = a[i][0]
                    a[i + j][1] = a[i][1].copy()
                elif a[i][0] == a[i + j][0]:
                    if len(a[i][1]) < len(a[i + j][1]):
                        a[i + j][1] = a[i][1].copy()


    return a[n-1][0], a[n-1][1]

if __name__ == "__main__":
    n = list(map(int, input().split()))
    b = list(map(int, input().split()))
    o = f(n[0], n[1], b)
    print(o[0])
    print(len(o[1]))
    o[1].append(n[0] - 1)
    print(" ".join([str(i + 1) for i in o[1]]))