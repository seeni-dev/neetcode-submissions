class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.minDistanceHelper(word1, word2, {})
    def getCache(self, word1, word2, dp):
        if word1 in dp and word2 in dp[word1]:
            return dp[word1][word2]
        return None

    def putCache(self, word1, word2, v, dp):
        if word1 not in dp:
            dp[word1] = {}
        dp[word1][word2] = v

    def minDistanceHelper(self, word1: str, word2: str, dp) -> int:
        c = self.getCache(word1, word2, dp)
        if c is not None:
            return c
        if word1 == word2:
            self.putCache(word1, word2, 0, dp)
            return 0
        if not len(word1):
            return len(word2)
        if not len(word2):
            return len(word1)
        i = 0
        matched = True
        while matched and i < len(word1) and i < len(word2):
            matched = word1[i] == word2[i]
            if matched:
                i+=1
        choices = []
        # Insert a character
        choices.append(1+self.minDistanceHelper(word1[i:], word2[i+1:], dp))

        # delete a character
        if i < len(word1):
            choices.append(1+self.minDistanceHelper(word1[i+1:], word2[i:], dp))

        if i < len(word1):
            choices.append(1+self.minDistanceHelper(word1[i+1:], word2[i+1:], dp))
        v = min(choices)
        self.putCache(word1, word2, v, dp)
        return v