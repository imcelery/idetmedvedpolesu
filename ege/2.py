for n in range(2):
    for k in range(2):
        for m in range(2):
            for l in range(2):
                o = not(n) or k and not(m) or (l == m)
                if not o:
                    print(n, k, m, l, int(o))
