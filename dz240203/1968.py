class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        mid = n // 2
        a = [0] * n
        for i in range(n):
            if i % 2:
                a[i] = nums[i // 2]
            else:
                a[i] = nums[i // 2 + mid]
        return a