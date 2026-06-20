from collections import defaultdict
class Solution:
    def numDecodings(self, s: str) -> int:
        s = list(map(int, list(s)))
        dp = defaultdict(lambda : 0)
        dp[len(s)] = 1
        for i in range(len(s)-1, -1, -1):
            if s[i] == 0:
                continue
            
            # Choice 1 character
            dp[i] = dp[i+1]
            
            # Choice 2 characters
            if i + 1 < len(s) and s[i] * 10 + s[i+1] <= 26:
                dp[i] += dp[i+2]
        return dp[0]
        