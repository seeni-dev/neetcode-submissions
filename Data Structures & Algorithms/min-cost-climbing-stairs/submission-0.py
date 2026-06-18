class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        dp[0] = 0
        dp[1] = 0
        for i in range(2, len(cost)+1):
            s1 = i - 1
            s2 = i - 2
            dp[i] = min(dp[s1] + cost[s1], dp[s2] + cost[s2])
        return dp[len(cost)]