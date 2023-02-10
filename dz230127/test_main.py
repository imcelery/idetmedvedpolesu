from unittest import TestCase
from main import *


class Testbfs(TestCase):
    def setUp(self) -> None:
        self.dict = {1:[2, 3, 5], 2:[1, 8, 10], 3:[1, 5, 7], 4 : [],  5:[1, 3], 6:[7, 10], 7:[10, 3], 8:[2], 9:[10], 10:[2,6,7,9]}
    def test_bfs1(self):
        self.assertEqual(bfs(self.dict, 1, 8), [1, 2, 8])

    def test_bfs2(self):
        self.assertEqual(bfs(self.dict, 4, 9), 'нет такого')


class Testdfs(TestCase):
    def setUp(self) -> None:
        self.dict = {1: [2, 3, 5], 2: [1, 8, 10], 3: [1, 5, 7], 4 : [], 5: [1, 3], 6: [7, 10], 7: [10, 3], 8: [2],
                     9: [10], 10: [2, 6, 7, 9]}

    def test_dfs1(self):
        self.assertEqual(dfs(self.dict, 1, 8), [1, 2, 8])

    def test_dfs2(self):
        self.assertEqual(dfs(self.dict, 4, 9), 'нет такого')
