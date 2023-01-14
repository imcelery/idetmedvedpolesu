from unittest import TestCase
from main import DoubleLinkedList, Stack, Queue


class TestDoubleLinkedList(TestCase):
    def setUp(self) -> None:
        self._linkedList = DoubleLinkedList()
        self._linkedList.append(1)
        self._linkedList.append(2)
        self._linkedList.append(3)

    def test_append(self):
        self._linkedList.append(4)
        self.assertEqual(self._linkedList.show(), "1 2 3 4")

    def test_remove(self):
        self._linkedList.remove(1)
        self.assertEqual(self._linkedList.show(), "1 3")

    def test_insert(self):
        self._linkedList.insert(1, 4)
        self.assertEqual(self._linkedList.show(), "1 2 4 3")

    def test_get(self):
        self.assertEqual(self._linkedList.get(1), 2)


class TestStack(TestCase):
    def setUp(self) -> None:
        self._stack = Stack()
        self._stack.push(1)
        self._stack.push(2)
        self._stack.push(3)


    def test_push(self):
        self._stack.push(4)
        self.assertEqual(self._stack.show(), "1 2 3 4")

    def test_pop(self):
        self._stack.pop()
        self.assertEqual(self._stack.show(), "1 2")

    def test_top(self):
        self.assertEqual(self._stack.top(), 3)

    def test_len(self):
        self.assertEqual(self._stack.len(), 3)

class TestQueue(TestCase):
    def setUp(self) -> None:
        self._queue = Queue()
        self._queue.push(1)
        self._queue.push(2)
        self._queue.push(3)


    def test_push(self):
        self._queue.push(4)
        self.assertEqual(self._queue.show(), "1 2 3 4")

    def test_pop(self):
        self._queue.pop()
        self.assertEqual(self._queue.show(), "2 3")

    def test_top(self):
        self.assertEqual(self._queue.top(), 1)

    def test_len(self):
        self.assertEqual(self._queue.len(), 3)
