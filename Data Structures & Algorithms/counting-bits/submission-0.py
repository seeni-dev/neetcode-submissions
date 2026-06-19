class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = {0: 0, 1: 1}
        for i in range(2, n+1):
            dp[i] = (i & 1) + dp[i>>1]
            print(dp)
        return [dp[i] for i in range(n+1)]