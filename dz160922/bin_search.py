def binsearch(a: list, el) -> int:
    start = 0
    finish = len(a) - 1
    i = 0
    while start <= finish:
        i = (finish + start) // 2
        if a[i] == el:
            return i
        elif a[i] > el:
            finish = i - 1
        elif a[i] < el:
            start = i + 1
    if a[i] < el:
        return i
    elif i > 0:
        return i - 1
    else:
        return 0

def binsearch_r(a: list, el, start, finish) -> int:
    i = (finish + start) // 2
    if start < finish:
        if a[i] == el:
            return i
        elif a[i] > el:
            return binsearch_r(a, el, start, i - 1)
        elif a[i] < el:
            return binsearch_r(a, el, i + 1, finish)
    else:
        if a[i] < el:
            return i
        elif i > 0:
            return i - 1
        else:
            return 0
