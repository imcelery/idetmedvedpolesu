import unittest
from search import linsearch
from search import linsearch_f
import time

class Test(unittest.TestCase):
    def setUp(self):
        self.a = [1, 2 ,3 ,4]

    def test_linsearch(self):
        self.assertEqual(linsearch(self.a, 2) ,1)

    def test_linsearch2(self):
        a = list(range(100000))
        t1 = time.time()
        i = linsearch(a, -1)
        t2 = time.time()
        self.assertLessEqual(t2 - t1, 0.01)

class Test2(unittest.TestCase):
    def setUp(self):
        self.a = [1.0, 2.009, 3.8, 4.0, -1000.01]

    def test_linsearch_f(self):
        self.assertEqual(linsearch_f(self.a, 2.010), 1)

    def test_linsearch_f2(self):
        self.assertNotEqual(linsearch_f(self.a, 2.011), 1)

    def test_linsearch_f3(self):
        self.assertIsNone(linsearch_f(self.a, -3))

    def test_linsearch_f4(self):
        self.assertEqual(linsearch_f(self.a, -1000.009), 4)


