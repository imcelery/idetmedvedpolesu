
def f(n):
    for i in range(1, 10):
        for j in range(len(n)):
            if int(n[j]) == i:
                if len(n) > 2:
                    return n[j]
                else:
                    if j == 1:
                        return n[j]

if __name__ == '__main__':
        n = int(input())
        for i in range(n):
            print(f(input()))

