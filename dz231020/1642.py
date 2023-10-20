class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        def canwe(i):
            s = sorted(a[:i+1])
            if ladders == 0:
                return sum(s) <= bricks
            return sum(s[:-ladders]) <= bricks
            
        a = [0]
        for i in range(len(heights) - 1):
            a.append(max(heights[i + 1] - heights[i], 0))
        l = 0
        r = len(a) - 1
        i = 0
        while l < r:
            i = (l + r) // 2
            if canwe(i):
                l = i + 1
            else:
                r = i - 1
        i = (l + r) //2
        if canwe(i):
            return i
        else:
            return i - 1