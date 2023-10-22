class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n = [1 for i in range(len(rooms))]
        n[0] = 0
        def f(l):
            for i in l:
                if n[i]:
                    n[i] = 0
                    f(rooms[i])
        f(rooms[0])
        return sum(n) == 0
