class Solution:
    def calculate(self, s: str) -> int:
        c = -1
        a = []
        for i in s:
            if i in ('+', '-', '*', '/'):
                if c != -1:
                    a.append(c)
                    c = -1
                a.append(i)
            elif i != " ":
                if c == -1:
                    c = int(i)
                else:
                    c = c * 10 + int(i)
        a.append(c)
        i = 1
        while i < len(a) - 1:
            if a[i] == "*":
                a[i + 1] = a[i - 1] * a[i + 1]
                a[i - 1] = None
                a[i] = None
            elif a[i] == "/":
                a[i + 1] = a[i - 1] // a[i + 1]
                a[i - 1] = None
                a[i] = None
            i += 2

        a = list(filter(lambda a: a != None, a))
        c = a[0]
        i = 1
        while i < len(a):
            if a[i] == "+":
                c += a[i + 1]
            elif a[i] == "-":
                c -= a[i + 1]
            i += 2
        return c