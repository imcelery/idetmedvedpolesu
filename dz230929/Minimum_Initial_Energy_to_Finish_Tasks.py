class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        l = max(sum(nums) // k, max(nums))
        r = sum(nums)
        i = (l + r) // 2

        def canWe(x, nums, k):
            s = 0
            for i in nums:
                if s + i <= x:
                    s += i
                elif i <= x:
                    k -= 1
                    if k < 0:
                        return False
                    s = i
                else:
                    return False
            if s <= x and k > 0:
                return True
            if s == 0 and k == 0:
                return True
            return False

        while l < r:
            i = (l + r) // 2
            if canWe(i, nums, k):
                r = i - 1
            else:
                l = i + 1

        if canWe(i, nums, k):
            i -= 1
            while canWe(i, nums, k):
                i -= 1
            return i + 1
        else:
            while not canWe(i, nums, k):
                i += 1
            return i
