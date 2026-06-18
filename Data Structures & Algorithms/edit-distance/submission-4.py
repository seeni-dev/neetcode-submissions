class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.minDistanceHelper(word1, word2, {}, 0, 0)
    def getCache(self, dp, i, j):
        if i in dp and j in dp[i]:
            return dp[i][j]
        return None

    def putCache(self, dp, i, j, v):
        if i not in dp:
            dp[i] = {}
        dp[i][j] = v

    def minDistanceHelper(self, word1: str, word2: str, dp, i, j) -> int:
        c = self.getCache(dp, i, j)
        if c is not None:
            return c
        res = None
        if word1[i:] == word2[j:]:
            res = 0
        if not len(word1[i:]):
            res = len(word2[j:])
        if not len(word2[j:]):
            res = len(word1[i:])
        if i < len(word1) and j < len(word2) and word1[i] == word2[j]:
            res = self.minDistanceHelper(word1, word2, dp, i+1, j+1)
        if res is not None:
            self.putCache(dp, i, j, res)
            return res
        
        choices = []
        # Insert a character
        choices.append(1+self.minDistanceHelper(word1, word2, dp, i, j+1))

        # delete a character
        if i < len(word1):
            choices.append(1+self.minDistanceHelper(word1, word2, dp, i+1, j))

        if i < len(word1):
            choices.append(1+self.minDistanceHelper(word1, word2, dp, i+1, j+1))
        v = min(choices)
        self.putCache(dp, i, j, v)
        return v