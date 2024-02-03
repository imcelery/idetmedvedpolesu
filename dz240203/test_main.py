from unittest import TestCase
from main import f


class Test(TestCase):
    def test_f(self):
        a = f()
        self.assertEquals(None, a)
