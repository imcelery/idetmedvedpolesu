class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        b = -1
        ls = -1
        maxs = 0
        mins = 0
        for i in range(n):
            a = sum([int(x) for x in bin(nums[i])[2:]])
            print(a)
            if a == b:
                maxs = max(maxs, nums[i])
                mins = min(mins, nums[i])
            else:
                if ls > mins:
                    break
                ls = maxs
                maxs = nums[i]
                mins = nums[i]
                b = a
        else:
            if ls > mins:
                return False
            else:
                return True
        return False