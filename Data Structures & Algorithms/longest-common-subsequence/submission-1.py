# cat
# crabt

from collections import defaultdict
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.longestCommonSubsequenceHelper(text1, text2, defaultdict(lambda : {}))
        
    def longestCommonSubsequenceHelper(self, text1: str, text2: str, dp) -> int:
        if text1 in dp and text2 in dp[text1]:
            return dp[text1][text2]
        if not text1 or not text2:
            return 0
        choices = []
        if text1[0] == text2[0]:
            choices.append(1+ self.longestCommonSubsequenceHelper(text1[1:], text2[1:], dp))
        else:
            choices.append(self.longestCommonSubsequenceHelper(text1[1:], text2, dp))
            choices.append(self.longestCommonSubsequenceHelper(text1, text2[1:], dp))
        dp[text1][text2] = max(choices)        
        return dp[text1][text2]