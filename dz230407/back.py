
def back(n):
    a = 1
    an = 1

    l = 2

    while a < n:
        a, an = an + a,  a

        l += 1


    if a == n:
        return l
    else:
        return -1

if __name__ == "__main__":
    n = int(input())

    print(back(n))
