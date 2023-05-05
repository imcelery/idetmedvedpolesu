import collections
#
#
# def obhod(d, s, was, cyc):
#
#     if s not in was:
#         was.append(s)
#         for i in d[s]:
#             if i in was:
#
#                 if (len(was) - was.index(i)) % 2 == 1:
#                     return False
#                 else:
#                     cyc.append(was[was.index(i):])
#             s = obhod(d, i, was.copy(), cyc)
#             if s == False:
#                 return False
#
#     return cyc
#
# def obhod2(d, s, was):
#     if s not in was:
#         was.add(s)
#         for i in d[s]:
#             was.update(obhod2(d, i, was))
#     return was
#
#
#
#
# if __name__ == '__main__':
#     n, m = list(map(int, input().split()))
#
#     if m == 0:
#         print("YES")
#     else:
#
#         a = []
#         d = collections.defaultdict(list)
#         for i in range(m):
#             n1, n2 = list(map(int, input().split()))
#             d[n1].append(n2)
#
#             d[n2].append(n1)
#
#         l = []
#
#         for i in range(1, n + 1):
#             g = obhod(d, 1, [], [])
#
#             if g == False:
#                 print('NO')
#                 break
#             else:
#                 if g not in l:
#                     l.append(g)
#         if len(l) > 0:
#             print("YES")
#             c = 0
#             waswas = set()
#             mout = []
#             for i in range(1, n + 1):
#                 was = set()
#                 w = obhod2(d, i, was)
#                 mw = min(w)
#
#                 if mw not in waswas:
#                     waswas.add(mw)
#                     c += len(w) // 2
#             print(c)

def obhod2(d, s, b , was):
    if s not in was:
        was.add(s)
        for i in d[s]:
            if i == b:
                return True
            f = obhod2(d, i, b, was)
            if f == True:
                return True

            was.update(f)
    return was

n, m = list(map(int, input().split()))

if m == 0:
    print("YES")
else:

    a = []
    d = collections.defaultdict(list)
    for i in range(m):
        n1, n2 = list(map(int, input().split()))
        d[n1].append(n2)

        d[n2].append(n1)
def f():
    a1 = []
    a2 = []
    for i in d.keys():
        if i in a1:
            if i in a2
