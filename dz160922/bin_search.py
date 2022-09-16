def binsearch(a: list, s) -> int:
    start = 0
    finish = len(a) - 1

    while start <= finish:

        sred = (finish + start) // 2
        if a[sred] > s:
            finish = sred - 1
        elif a[sred] < s:
            start = sred + 1
        else:
            return sred

def binsearch_r(a: list, el, s, f) -> int:
    i = int(len(a)//2)
    if a[i] == el:
        return i
    elif a[i] > el:
        f = i
        return binsearch_r(a[:i], el, s, f)
    else:
        s = i
        return binsearch_r(a[i:], el, s, f)