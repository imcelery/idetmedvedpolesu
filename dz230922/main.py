class Solution:
           
    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @cache
        def getPower(x):
            if x == 1:
                return 0
            if x % 2==0:
                return 1 + getPower(x // 2)
            else:
                return 1 + getPower(3  * x + 1)

        k -= 1
        d = {}
        for i in range(hi - lo + 1):
            x = i + lo
            c = getPower(x)
            if c in d.keys():
                d[c].append(i + lo)
            else:
                d.update({c : [i + lo]})

        for i in sorted(d.keys()):
            if k >= len(d[i]):
                k -= len(d[i])
            else:
                return d[i][k]