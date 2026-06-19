class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = self.longestPalindromeHelper(s, 0, len(s)-1, {})
        return s[t[0]:t[1]+1]
    
    def longestPalindromeHelper(self, s: str, i: int, j: int, dp = {}) -> str:
        t = (i, j,)
        l = j - i + 1
    
        if t in dp:
            return dp[t]
    
        if l < 1:
            dp[t] = t
            return t
        
        choices = []
        if s[i] == s[j]:
            rs = (i+1, j-1)
            rl = self.longestPalindromeHelper(s, i+1, j-1, dp)
            if rl == rs:
                dp[t] = t
                return t
            else:
                choices.append(rl)
        choices.append(self.longestPalindromeHelper(s, i+1, j, dp))
        choices.append(self.longestPalindromeHelper(s, i, j-1, dp))
        res = None
        resLength = 0
        for e in choices:
            eLength = e[1] - e[0] + 1
            if res is None or eLength > resLength:
                res = e
                resLength = eLength
        dp[t] = res
        return res
            
            