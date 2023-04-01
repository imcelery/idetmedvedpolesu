def print_hi(name):
    a = []
    n = False

    k = 0
    sum = 0
    with open(name) as f:
        for i in f.readlines():
            if not n:
                n = True
            else:
                num = int(i)
                a.append(num)
                if num % 2 == 1:
                    k += 1
                sum += num

    if k % 10 == 0:
        return sum

    else:
        d = k % 10
        smin = 0
        for i in range(d):
            s = sum

            k = 0
            j = 0
            while k < i:
                s -= a[j]
                if a[j] % 2 == 1:
                    k += 1
                j += 1

            k = 0
            j = 1

            while k < d - i:
                s -= a[len(a) - j]
                if a[len(a) - j] % 2 == 1:
                    k += 1
                j += 1
            smin = max(s, smin)

        return smin

if __name__ == '__main__':
    print( print_hi('C:/Users/mushnikov/Downloads/27-B.txt'))
