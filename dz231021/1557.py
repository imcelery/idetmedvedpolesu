class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        o = list(range(n))
        for i in edges:
            o[i[1]] = -1
        oo = []
        for i in o:
            if i != -1:
                oo.append(i)
        return oo
