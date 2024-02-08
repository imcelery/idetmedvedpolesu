class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        s = 0
        x, y = point

        for (xn, yn), n in self.points.items():
            if xn != x and abs(x - xn) == abs(y - yn):
                if (x, yn) in self.points and (xn, y) in self.points:
                    s += n * self.points[(x, yn)] * self.points[(xn, y)]
        return s


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)