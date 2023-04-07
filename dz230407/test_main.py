from unittest import TestCase
from main import forward
from back import back
from len import lenn

class Test(TestCase):

    def test_forward1(self):
        n = 21
        self.assertEqual(forward(n), 8)

    def test_forward2(self):
        n = 17
        self.assertEqual(forward(n), -1)

    def test_back1(self):
        n = 21
        self.assertEqual(back(n), 8)

    def test_back2(self):
        n = 17
        self.assertEqual(back(n), -1)

    def test_lenn1(self):
        n = 21
        self.assertEqual(lenn(n), 8)

    def test_lenn2(self):
        n = 17
        self.assertEqual(lenn(n), -1)
