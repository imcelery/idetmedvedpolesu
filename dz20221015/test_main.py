from unittest import TestCase
from main import Digital
import random


class TestDigital(TestCase):
    def setUp(self):
        self.digital = Digital()
        self.decArray = [random.randint(0, 1000) for _ in range(1000)]
        self.decArrayFloat = [10.25, 3.875, 0.5]
        self.binArray = [bin(i)[2:] for i in self.decArray]
        self.binArrayFloat = ["1010.01", "11.111", "0.1"]

    def test_dec_to_bin(self):
        b = []
        for i in self.decArray:
            b.append(self.digital.dec_to_bin(i))
        self.assertEqual(b, self.binArray)

    def test_dec_to_bin_float(self):
        b = []
        for i in self.decArrayFloat:
            b.append(self.digital.dec_to_bin_float(i))
        self.assertEqual(b, self.binArrayFloat)

    def test_bin_to_dec(self):
        b = []
        for i in self.binArray:
            b.append(self.digital.bin_to_dec(i))
        self.assertEqual(b, self.decArray)

    def test_bin_to_dec_float(self):
        b = []
        for i in self.binArrayFloat:
            b.append(self.digital.bin_to_dec_float(i))
        self.assertEqual(b, self.decArrayFloat)