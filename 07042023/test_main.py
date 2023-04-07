from unittest import TestCase
from main import forward

class Test(TestCase):

    def test_forward1(self):
        n = 21
        self.assertEqual(forward(n), 8)

    def test_forward2(self):
        n = 17
        self.assertEqual(forward(n), -1)
