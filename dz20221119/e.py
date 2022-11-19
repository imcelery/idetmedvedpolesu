def beaty(l, d):
    a = 0
    for i in range(2, len(l)):
        for j in range(i - 1, 0, -1):
            if l[i] - l[j] < d:
                for k in range(j - 1, -1, -1):
                    if l[i] - l[k] <= d:
                        a += 1
                    else:
                        break
            else:
                break
    return a


if __name__ == '__main__':
        a = input().split()
        q, d = int(a[0]), int(a[1])
        z = input().split()
        zz = []
        for i in z:
            zz.append(int(i))
        print(beaty(zz, d))

