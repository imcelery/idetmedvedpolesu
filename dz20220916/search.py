def linsearch(a:list, s)->int:
    for i, el in enumerate(a):
        if el == s:
            return i

def linsearch_f(a:list, s)->int:
    for i, el in enumerate(a):
        if abs(el - s) <= 0.001:
            return i