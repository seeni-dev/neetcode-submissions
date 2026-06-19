class Solution:
    def longestPalindrome(self, s: str, dp = {}) -> str:
        if s in dp:
            return dp[s]
        if len(s) < 1:
            dp[s] = s
            return s
        
        choices = []
        if s[0] == s[-1]:
            rs = s[1:-1]
            rl = self.longestPalindrome(rs)
            if rl == rs:
                dp[s] = s
                return s
            else:
                choices.append(rl)
        choices.append(self.longestPalindrome(s[1:]))
        choices.append(self.longestPalindrome(s[:-1]))
        res = choices[0]
        for i in range(1, len(choices)):
            e = choices[i]
            if len(e) > len(res):
                res = e
        dp[s] = res
        return res
            
            