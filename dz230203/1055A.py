def deepseaaarch(pos, s, a, b, g):
    if pos == s:
        return "YES"
    else:
        g.append(pos)
        for i in range(len(a)):
            if a[i] == 1 and i not in g and i > pos:
                g.append(i)
                d = deepseaaarch(i, s, a, b, g)
                if d == "YES":
                    return "YES"
                else:
                    g.extend(d)

        for i in range(len(b)):
            if b[i] == 1 and i not in g and i < pos:
                g.append(i)
                d = deepseaaarch(i, s, a, b, g)
                if d == "YES":
                    return "YES"
                else:
                    g.extend(d)

        return g



if __name__ == '__main__':
    n = [int(i) - 1 for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    if a[0] == 1:
        d = deepseaaarch(0, n[1], a, b, [])
        if d == "YES":
            print("YES")
        else:
            print("NO")
    else:
        print("NO")