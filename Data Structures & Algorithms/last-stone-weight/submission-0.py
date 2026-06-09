import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) >= 2:
            x,y = heapq.heappop_max(stones), heapq.heappop_max(stones)
            dx = abs(x-y)
            if dx:
                heapq.heappush_max(stones, dx)
        return 0 if not stones else stones[0]