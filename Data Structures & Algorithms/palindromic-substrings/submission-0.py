# dp[i] = 
# number of palindroms at dp[i-1] + 1 if s[:i] is a Palndrome + 1
class Solution:
    def isPalindrome(self, s: int, i: int, j: int):
        res = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            res += 1
            i -= 1
            j +=1
        return res
    def countSubstrings(self, s: str) -> int:
        r = 0
        for i in range(len(s)):
            r += self.isPalindrome(s, i, i)
            r += self.isPalindrome(s, i, i+1)
        return r
        