def print_hi(name):
    smax = 0
    smin = 0

    a2 = []
    a3 = []
    a4 = []
    n = False

    with open(name) as f:
        for i in f.readlines():
            if not n:
                n = True
            else:
                s = [int(j) for j in i.split()]
                if s[1] % 2 == 1:
                    b = sorted(s)
                    smax += b[1]
                    smin += b[0]
                    if b[1] % 2 == 1 and b[0] % 2 == 0:
                        a2.append(b[0] + b[1])
                    elif b[1] % 2 == 0 and b[0] % 2 == 1:
                        a3.append(b[0] + b[1])
                    elif b[1] % 2 == 1 and b[0] % 2 == 1:
                        a4.append(b[0] + b[1])
    a2 = min(a2)
    a3 = min(a3)
    if len(a4) > 0:
        a4 = min(a4)
    else:
        a4 = 20001

    if smax % 2 == 0 and smin % 2 == 0:
        return max(smin + smax - a3, smin + smax - a2 - a4)

    elif smax % 2 == 1 and smin % 2 == 0:
        return max(smin + smax - a4, smin + smax - a3 - a2)

    elif smax % 2 == 0 and smin % 2 == 1:
        return smin + smax

    elif smax % 2 == 1 and smin % 2 == 1:
        return max(smin + smax - a2, smin + smax - a3 - a4)

if __name__ == '__main__':
    print( print_hi('C:/Users/mushnikov/Downloads/inf_26_04_21_27b.txt'))
