class Solution:
             
    def getKth(self, lo: int, hi: int, k: int) -> int:
        d = {}
        def getPower(x, d):
            if x in d.keys():
                return d[x]

            elif x != 1: 
                if x % 2==0:
                    c = 1 + getPower(x // 2, d)
                    d.update({x : c})
                    return c
                else:
                    c = 1 + getPower(x * 3 + 1, d)
                    d.update({x : c})
                    return c
            return 0

        a = []

        for i in range(hi - lo + 1):
            a.append([0, 0])
            x = i + lo
            c = getPower(x, d)
            a[i][0] = c
            a[i][1] = i + lo
        a.sort(key=lambda x: x[0])
        return a[k - 1][1]