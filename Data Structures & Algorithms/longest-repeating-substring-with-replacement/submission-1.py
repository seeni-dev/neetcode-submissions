# XYASBDYX, 2
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        countHash = defaultdict(lambda : 0)
        maxCount = 0
        windowStart = 0
        for i, c in enumerate(s):
            countHash[c] += 1
            maxCount = max(maxCount, countHash[c])

            if (i-windowStart+1 - maxCount) > k:
                countHash[s[windowStart]] -=1
                windowStart += 1
            
            maxLength = max(maxLength, i-windowStart + 1)
        return maxLength
