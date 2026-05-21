from collections import defaultdict
class Solution:
    def climbStairs(self, n: int) -> int:
        d = {}
        d[1] = 1
        d[2] = 2
        for j in range(3, n+1):
            d[j] = d[j-1] + d[j-2]
        return d[n]
        