from collections import defaultdict


class Solution:
    def sortItems(self, n: int, m: int, group: list[int], beforeItems: list[list[int]]) -> list[int]:
        def top_sort(grap, x, visited, output):
            if visited[x] == 1:
                return False
            if visited[x] == 2:
                return True

            visited[x] = 2
            for i in grap[x]:
                if top_sort(grap, i, visited, output):
                    return True
            output.append(x)
            visited[x] = 1
            return False

        items_grups = defaultdict(list)
        visited_items = defaultdict(dict)

        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
            items_grups[group[i]].append(i)
            visited_items[group[i]][i] = 0

        group_grap = defaultdict(list)
        item_grap = {i: defaultdict(list) for i in range(m)}

        for i in range(len(beforeItems)):
            after = group[i]
            for j in beforeItems[i]:
                before = group[j]

                if before != after:
                    group_grap[before].append(after)
                else:
                    item_grap[before][j].append(i)

        res = []
        vis = [0] * m
        for i in range(m):
            if top_sort(group_grap, i, vis, res):
                return []

        resres = []

        for i in res:
            for j in items_grups[i]:
                if top_sort(item_grap[i], j, visited_items[i], resres):
                    return []
        return resres[::-1]

n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
s = Solution()
print(s.sortItems(n, m, group, beforeItems))