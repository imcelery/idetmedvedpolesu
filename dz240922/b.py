import fileinput

def sortd(a, p, level = 0):

    if len(p) <= level:
        return a
    elif p[level] == 0:
        return sortd(a, p, level + 1)
    elif len(a) <= 1:
        return a

    elif p[level] == 1:

        a.sort(key=lambda i: i[level])
        b = a[0]
        c = []
        newa = []
        for i in a:
            if b[level] != i[level]:
                newa = newa + sortd(c, p, level + 1)
                b = i
                c = []
                c.append(i)
            else:
                c.append(i)
        newa = newa + sortd(c, p, level + 1)
        return newa


    elif p[level] == -1:
        a.sort(key=lambda i: i[level], reverse=True)
        b = a[0]
        c = []
        newa = []
        for i in a:
            if b[level] != i[level]:
                newa = newa + sortd(c, p, level + 1)
                b = i
                c = []
                c.append(i)
            else:
                c.append(i)
        newa = newa + sortd(c, p, level + 1)
        return newa

d = {}
h = input().split(" ")
for i in h:
    d.update({i : 0})

a = input()
a = a.replace(',',"").split()
for i in range(len(a)):
    if i % 2 == 1:
        if a[i] == "ASC":
            d[a[i - 1]] = 1
        elif a[i] == "DESC":
            d[a[i - 1]] = -1
tab = []
p = []

for i in h:
    p.append(d.get(i))

for line in fileinput.input():
    l = line.strip().split(" ")
    tab.append(l)

tab = sortd(tab, p)
for i in range(len(tab)):
    print(" ".join(tab[i]))