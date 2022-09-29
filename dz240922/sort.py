def search_min(a, start):
    m = a[start]
    min_i = start
    for i in range(start, len(a)):
        if a[i] < m:
            m  = a[i]
            min_i = i
    return min_i

def sort_vi(a):
    for i in range(len(a) - 1):
        m_i = search_min(a, i)
        a[i], a[m_i] = a[m_i], a[i]
    return a

def sort_p(a):
    for i in range(len(a) - 1):
        xi = i
        for j in range(i + 1, len(a)):
            if a[xi] > a[j]:
                a[xi], a[j] = a[j],  a[xi]
    return a

def sort_v(a):
    for i in range(1, len(a)):
        xi = i
        for j in range(i - 1, -1, -1):
            if a[j] > a[xi]:
                a[j], a[xi] = a[xi], a[j]
                xi -= 1
            else:
                break
    return a

def serge(a, b):
    ai = 0
    bi = 0
    c = []
    while ai < len(a) and bi < len(b):
        if a[ai] <= b[bi]:
            c.append(a[ai])
            ai += 1
        else:
            b.append(b[bi])
            bi += 1
    while ai < len(a):
        c.append(a[ai])
        ai += 1
    while bi < len(b):
        c.append(b[bi])
        bi += 1
    return c

def sort_serge(a):
    if len(a) <= 1:
        return a
    k = len(a) //2
    b1 = sort_serge(a[:k])
    b2 = sort_serge(a[k:])
    return serge(b1, b2)