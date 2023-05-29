class sol:
    def __init__(self):
        self.s = 0
    def f(self, x, n, m):
        def ff(x):
            if x == m:
                return None
            if x == n:
                self.s += 1
            if x < n:
                ff(x + 1)
                ff(x * 2)
        ff(x)
        o = self.s
        self.s = 0
        return o

s = sol()
print(s.f(1, 9, 10) * s.f(9, 20, 10) + s.f(1, 10, 9) * s.f(10, 20, 9))

