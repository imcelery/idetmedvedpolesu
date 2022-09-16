from unittest import TestCase
from bin_search import *


class Test(TestCase):
    def setUp(self) -> None:
        self.a = [1, 3, 5]
    def test_binsearch(self):
        self.assertEqual(binsearch(self.a, 5) ,2)
