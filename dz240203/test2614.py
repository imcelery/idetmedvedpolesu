from math import sqrt
from unittest import TestCase
#ВРОДЕ НОРМ
def diagonalPrime(nums: list[list[int]]) -> int:
    listi = []
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            if i == j:
                listi.append(nums[i][j])
                listi.append(nums[i][len(nums)-1-i])

    ans = 0

    for i in range(len(listi)):
            for j in range(2, int(sqrt(listi[i]))+1):
                if listi[i] % j == 0:
                    break
            else:
                if listi[i] > ans:
                    ans=listi[i]

    if ans == 1:
        return 0
    return ans

class Test(TestCase):
    def test_f(self):
        a = diagonalPrime([[1, 2, 17], [2, 5, 6], [10, 10, 10]])
        self.assertEqual(17, a)

    def test_f1(self):
        a = diagonalPrime([[]])
        self.assertEqual(0, a)
