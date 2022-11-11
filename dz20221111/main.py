def factor(n):
    a = 0
    b = 1
    while  n - a > 1:
        b *= n-a
        a += 1
    return(b)

def factor2(n, k):
    a = 0
    b = 1
    while n - a > k:
        b *= n - a
        a += 1
    return (b)

def c(k, n):
    if k > n-k:
        return factor2(n, k) // factor(n-k)
    else:
        return factor2(n, n - k) // factor(k)

shag_i = 20000
shaj_j = 22000

i = 20000
j = 1
while True:
    while True:
        print(j, i, c(j, i))
        if j + shaj_j > i:
            break
        else:
            j += shaj_j
    i += shag_i
    j = 1

