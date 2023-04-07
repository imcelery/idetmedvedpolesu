
def forward(n):
    a = 1
    an = 1

    l = 2

    def getnew(a, an):
        return an, a + an



    while an < n:
        a, an = getnew(a, an)
        l += 1


    if an == n:
        return l
    else:
        return -1




if __name__ == "__main__":
    n = int(input())

    print(forward(n))
