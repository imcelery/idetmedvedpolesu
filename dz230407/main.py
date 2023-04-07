
def forward(n):
    a = 1
    an = 1

    l = 2


    while an < n:
        a, an = an, a + an
        l += 1


    if an == n:
        return l
    else:
        return -1




if __name__ == "__main__":
    n = int(input())

    print(forward(n))
