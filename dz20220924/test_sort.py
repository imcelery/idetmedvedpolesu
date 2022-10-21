from unittest import TestCase
from sort import *


class Testvi(TestCase):
    def setUp(self) -> None:
        self.a = [1, 43, -32, 32, 2, 0]
        self.b =[i**2 for i in range(-23, 53)]
        self.c = [0]
    def test_sort_vi_1(self):
        self.assertEqual(sort_vi(self.a), sorted(self.a))
    def test_sort_vi_2(self):
        self.assertEqual(sort_vi(self.b), sorted(self.b))
    def test_sort_vi_3(self):
        self.assertEqual(sort_vi(self.c), sorted(self.c))

class Testp(TestCase):
    def setUp(self) -> None:
        self.a = [1, 43, -32, 32, 2, 0]
        self.b =[i**2 for i in range(-23, 53)]
        self.c = [0]
    def test_sort_p_1(self):
        self.assertEqual(sort_p(self.a), sorted(self.a))
    def test_sort_p_2(self):
        self.assertEqual(sort_p(self.b), sorted(self.b))
    def test_sort_p_3(self):
        self.assertEqual(sort_p(self.c), sorted(self.c))

