from unittest import TestCase
from main import Digital
import random


class TestDigital(TestCase):
    def setUp(self):

        self.digital = Digital()
        self.decArray = [random.randint(0, 10000) for _ in range(1000)]
        self.binArray = [bin(i)[2:] for i in self.decArray]

    def test_dec_to_bin(self):
        b = []
        for i in self.decArray:
            b.append(self.digital.dec_to_bin(i))
        self.assertEqual(b, self.binArray)

    def test_bin_to_dec(self):
        b = []
        for i in self.binArray:
            b.append(self.digital.bin_to_dec(i))
        self.assertEqual(b, self.decArray)