def print_hi(name):
    smax = 0
    smin = 0

    a1 = []
    a2 = []

    n = False

    with open(name) as f:
        for i in f.readlines():
            if not n:
                n = True
            else:
                s = int(i)
                if s % 2 == 1:
                    a1.append(s)
                else:
                    a2.append(s)
    s = 0
    m = 0


    a2 = sorted(a2)

    na = set(a1)

    ma = max(a1)

    for i in a1:
        for j in a2:

            if i + j > ma:
                break

            if i + j in na:
                s += 1
                m = max(m, i + j)

    return s, m

if __name__ == '__main__':
    print(print_hi('C:/Users/mushnikov/Downloads/inf_26_04_21_26.txt'))