from unittest import TestCase
from main import main


class Test(TestCase):
    def test_0(self):
        main("program0.txt", "out.txt")

    def test_1(self):
        main("program1.txt", "out.txt")

    def test_2(self):
        main("program2.txt", "out.txt")

    def test_3(self):
        main("program3.txt", "out.txt")

    def test_4(self):
        main("program4.txt", "out.txt")

    def test_5(self):
        main("program5.txt", "out.txt")

    def test_6(self):
        main("program6.txt", "out.txt")

    def test_7(self):
        main("program7.txt", "out.txt")

    def test_8(self):
        main("program8.txt", "out.txt")