class MyCalendarThree:
    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> int:
        bisect.insort(self.events, (startTime, 1))
        bisect.insort(self.events, (endTime, -1))
        s = 0
        mx = 0
        for i in self.events:
            s += i[1]
            mx = max(s, mx)
        return mx
