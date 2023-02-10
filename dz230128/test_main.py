from unittest import TestCase
from main import *

class TestGraph(TestCase):
    def setUp(self) -> None:
        self.g = Graph({1: [[2, 3], [3, 4]], 2: [[1, 3], [3, 7], [4, 9]], 3: [[2, 7], [1, 4], [4, 1]], 4: [[2, 9], [3, 1]]})
    def test_dijkstra1(self):
        self.assertEqual(self.g.dijkstra(1), {1: 0, 2: 3, 3: 4, 4: 5})

    def test_dijkstra2(self):
        self.assertEqual(self.g.dijkstra(2), {1: 3, 2: 0, 3: 7, 4: 8})
