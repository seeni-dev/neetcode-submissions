import heapq
from collections import defaultdict

class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        mp = defaultdict(lambda : 0)
        for xi, yi in zip(x,y):
            mp[xi] = max(mp[xi], yi)

        heap = []
        for v in mp.values():
            heapq.heappush(heap, v)
            if len(heap) > 3:
                heapq.heappop(heap)
        if len(heap) == 3:
            return sum(heap)
        return -1