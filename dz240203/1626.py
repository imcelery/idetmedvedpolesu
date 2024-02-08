class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        a = []
        n = len(scores)
        for i in range(n):
            a.append([ages[i], scores[i]])
        a.sort()
        nums = [x[1] for x in a]
        dp = [x[1] for x in a]
        for i in range(1, n):
            for j in range(i):
                if nums[i] >= nums[j]:
                    if dp[i] < dp[j] + nums[i]:
                        dp[i] = dp[j] + nums[i]
        return max(dp)