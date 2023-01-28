from unittest import TestCase
from main import first_unique_number, sort_stack, generate_binary_number, LinkedList, del_dublicate_linked_list
from collections import deque


class Test_first_unique_number(TestCase):
    def test_first_unique_number(self):
        self.assertEqual(first_unique_number([3, 6, 2, 2, 6, 7, 9, 2]), [3, 7, 9])


class Test_sort_stack(TestCase):
    def test_sort_stack(self):
        s = [3, 6, 2, 2, 6, 7, 9, 2]
        self.assertEqual(sort_stack(deque(s)), s.sort())


class Test_generate_binary_number(TestCase):
    def test_generate_binary_number(self):
        n = 16
        self.assertEqual(generate_binary_number(n),
                         ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010',
                          '1011', '1100', '1101', '1110', '1111'])


class Test_del_dublicate_linked_list(TestCase):
    def test_del_dublicate_linked_list(self):
        n = LinkedList([2,2,7,4,4])
        del_dublicate_linked_list(n)
        self.assertEqual(str(n), "2 -> 7 -> 4 -> None")