from functools import cache
class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        n = len(graph) - 1

        @cache
        def f(c):
            if c == n:
                return [[n]]
            o = []
            for i in graph[c]:
                for j in f(i):
                    o.append([c] + j)
            return o

        return f(0)
