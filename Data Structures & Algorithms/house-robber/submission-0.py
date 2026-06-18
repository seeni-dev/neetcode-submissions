from collections import defaultdict
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = defaultdict(lambda : 0)
        for i, n in enumerate(nums):
            dp[i] = max(
                dp[i-2] + nums[i],
                dp[i-1]
            )
        return dp[len(nums)-1]
        