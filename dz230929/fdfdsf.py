class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        def canWe(x, tasks):
            for i in tasks:
                if i[1] <= x:
                    x -= i[0]
                else:
                    return False
            if x >= 0:
                return True
            return False

        tasks.sort(key = lambda x : (x[1]-x[0]), reverse = True)

        l = 0
        r = 0
        for i in tasks:
            r += i[1]

        i = (l + r) // 2

        while l < r :
            i = (l + r) // 2
            if not canWe(i, tasks):
                l = i + 1
            else:
                r = i
        if canWe(i, tasks):
            if canWe(i - 1, tasks):
                return i - 1
            return i
        else:
            return i + 1