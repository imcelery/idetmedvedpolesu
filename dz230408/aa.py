#Из того что я (не)понял
#Алгоритм обрятный
#сложность - строка (n)


def f(n, k):

    if n == 1:
        if k > 9:
            return 0
        return 1
    if k == 0:
        return 1
    s = 0
    for i in range(min(k + 1, 10)):
        s += f(n - 1, k - i)
    return s
def fout(n):
    s = 0
    for i in range( 9 * n  + 1):

        s += f(n, i) ** 2
    return s



if __name__ == "__main__":
    n = int(input())
    print(fout(n//2))



