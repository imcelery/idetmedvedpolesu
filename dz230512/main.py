import math


class Tree:

    def __init__(self, nums: list[int]):
        self.h = math.ceil(math.log2(len(nums))) + 1
        self.k = 2 ** (self.h - 1)
        self.n = 2 ** self.h - 1
        self.tree = [0 for i in range(self.n)]
        self.a = nums
        self.built()

    def built(self):
        for i in range(len(self.a)):
            self.tree[self.n - self.k + i] = self.a[i]

        for i in range(self.n - self.k - 1, -1, -1):
            self.tree[i] = self.tree[i * 2 + 2] + self.tree[i * 2 + 1]

    def update(self, index: int, val: int) -> None:
        ind = 1 + index + self.n - self.k

        self.tree[ind - 1] = val


        for i in range(self.h, 1, -1):
            if ind % 2 == 1:
                tind = ind - 1
            else:
                tind = ind + 1

            self.tree[ind // 2 - 1] = self.tree[ind - 1] + self.tree[tind - 1]

            ind //= 2


    def sumRange(self, left: int, right: int) -> int:
        left += 1 + self.n - self.k
        right += 1 + self.n - self.k

        s = 0
        if left > right:
            return s

        if left == right:
            return self.tree[right - 1]

        while left <= right:
            if left % 2 == 1:
                s += self.tree[left - 1]
            if right % 2 == 0:
                s += self.tree[right - 1]
            left = (left + 1) // 2
            right = (right - 1) // 2

        return s





if __name__ == '__main__':
    t = Tree([1, 3, 5])
    print(t.sumRange(0, 2))
    t.update(1, 2);
    print(t.tree)
    print(t.sumRange(0, 2))


