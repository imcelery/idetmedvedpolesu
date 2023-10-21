class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for i in nums:
            i.sort()
        a = [0] * len(nums[0])
        for i in range(len(nums)):
            for j in range(len(a)):
                a[j] = max(a[j], nums[i][j])
        return sum(a)
        