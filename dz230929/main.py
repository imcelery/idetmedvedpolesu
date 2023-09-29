class Solution:
    def countRoutes(self, locations: list[int], start: int, finish: int, fuel: int) -> int:

        d = dict.fromkeys(list(range(len(locations))))
        if finish == start:
            finishKen = 1
        else:
            finishKen = 0

        for i in d.keys():
            d[i] = []
        for i in range(len(locations)):
            if i != start:
                if abs(locations[i] - locations[start]) <= fuel:
                    d[i].append(fuel - abs(locations[i] - locations[start]))
                    if i == finish:
                        finishKen += 1


        while True:
            b = False
            print(d)
            for i in d.keys():
                if len(d[i]) > 0:
                    b = True
                    v = d[i].pop()
                    for k in d.keys():
                        if k != i:
                            a = abs(locations[i] - locations[k])
                            if a <= v:
                                for o in range(1, v // a + 1, 2):
                                    d[k].append(v - a * o)
                                    if k == finish:
                                        finishKen += 1
            if not b:
                break
        return finishKen % 1000000007

s = Solution()
locations = [4, 3, 1]
start = 1
finish = 0
fuel = 6
print(s.countRoutes(locations, start, finish, fuel))