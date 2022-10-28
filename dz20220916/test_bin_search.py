from unittest import TestCase
from bin_search import *


class Test(TestCase):
    def setUp(self) -> None:
        self.a = [el**2 for el in range(28)]

    def test_binsearch(self):
        self.assertEqual(binsearch(self.a, 4), 2)

    def test_binsearch2(self):
        self.assertEqual(binsearch(self.a, 5), 2)

    def test_binsearch3(self):
        self.assertEqual(binsearch(self.a, -23), 0)

    def test_binsearch4(self):
        self.assertEqual(binsearch(self.a, 1000), 27)


class Test2(TestCase):
    def setUp(self) -> None:
        self.a = [el ** 2 for el in range(28)]

    def test_binsearch_r(self):
        self.assertEqual(binsearch_r(self.a, 4), 2)

    def test_binsearch_r2(self):
        self.assertEqual(binsearch_r(self.a, 5), 2)

    def test_binsearch_r3(self):
        self.assertEqual(binsearch_r(self.a, -23), 0)

    def test_binsearch_r4(self):
        self.assertEqual(binsearch_r(self.a, 1000), 27)


