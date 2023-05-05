import collections

def obhod(d, s, was):
    if s not in was:
        was.add(s)
        for i in d[s]:
            was.update(obhod(d, i, was))
    return was




if __name__ == '__main__':

    n, m = list(map(int, input().split()))
    if m == 0:
        print(n)
        for i in range(1, n + 1):
            print(1)
            print(i)
    else:
        a = []
        d = collections.defaultdict(list)
        for i in range(m):
            n1, n2 = list(map(int, input().split()))
            d[n1].append(n2)


            d[n2].append(n1)

        waswas = set()
        mout = []
        for i in range(1, n + 1):
            was = set()
            w = obhod(d, i, was)
            mw = min(w)


            if mw not in waswas:
                waswas.add(mw)
                mout.append(str(len(w)) + "\n" + " ".join(map(str, list(w))))

        print(len(mout))
        for i in mout:
            print(i)


    # was = set()
    #
    # print(len(obhod(d, s, was)))