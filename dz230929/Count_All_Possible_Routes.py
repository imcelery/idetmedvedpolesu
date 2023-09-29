class Solution:
    def countRoutes(self, loc: list[int], start: int, finish: int, fuel: int) -> int:
        @cache
        def detPaws(x, f):
            if x == finish:
                p = 1
            else:
                p = 0
            for i in range(len(loc)):
                if i != x:
                    a = abs(loc[i] - loc[x])
                    if a <= f:
                        p += detPaws(i, f - a)
            return p

        return detPaws(start, fuel) % 1000000007
