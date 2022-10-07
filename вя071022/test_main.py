from unittest import TestCase
from main import substring

class Test(TestCase):
    def test_substring(self):
        self.assertEqual(substring("332dssdddsfsdsfsadfs", "32dssdddsfsd"), [1])

    def test_substring2(self):
        self.assertEqual(substring("1", "3434"), [])

    def test_substring3(self):
        self.assertEqual(substring("aaaaa", "aa"), [0, 1, 2, 3])
