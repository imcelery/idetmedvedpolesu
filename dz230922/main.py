class Solution:
             
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def getPower(x):
            c = 0
            while x != 1:
                if x % 2==0:
                    x = x // 2
                else:
                    x = 3  *x + 1
                c+=1
            return c

        a = []

        for i in range(hi - lo + 1):
            a.append([0, 0])
            x = i + lo
            c = 0
            while x != 1:
                if x % 2==0:
                    x = x // 2
                else:
                    x = 3  *x + 1
                c+=1
            a[i][0] = c
            a[i][1] = i + lo
        a.sort(key=lambda x: x[0])
        return a[k - 1][1]