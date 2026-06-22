from collections import defaultdict
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = defaultdict(lambda : -1)
        for c in coins:
            dp[c] = 1
        dp[0] = 0
        for a in range(amount+1):
            choices = []
            for c in coins:
                r = a - c
                if r not in dp:
                    continue
                choices.append(dp[r] + 1)
            if choices:
                dp[a] = min(choices)
        return dp[amount]

        
        