from unittest import TestCase
#ВРОДЕ НОРМ
def sortPeople(names: list[str], heights: list[int]) -> list[str]:
    a = []
    for i in range(len(names)):
        a.append([heights[i], names[i]])
    a = sorted(a)[::-1]
    b = []
    for i in range(len(a)):
        b.append(a[i][1])
    return b

class Test(TestCase):
    def test_f(self):
        a = sortPeople([], [])
        self.assertEqual([], a)

    def test_f1(self):
        a = sortPeople(["a", "b", "v"], [3, 2, 1])
        self.assertEqual(["a", "b", "v"], a)

    def test_f2(self):
        a = sortPeople(["a", "v", "b"], [3, 1, 2])
        self.assertEqual(["a", "b", "v"], a)
