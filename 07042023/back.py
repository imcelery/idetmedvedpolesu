
def back(n):
    fib = [1, 0]

    def getnew(fib):
        fib[len(fib) - 1] += fib[len(fib) - 2]
        fib.append(fib[len(fib) - 2])
        return fib



    while fib[len(fib) - 2] < n:
        fib = getnew(fib)


    if fib[len(fib) - 2] == n:
        return len(fib) - 1
    else:
        return -1




if __name__ == "__main__":
    n = int(input())

    print(back(n))
