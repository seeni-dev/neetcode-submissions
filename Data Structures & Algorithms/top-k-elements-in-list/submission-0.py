import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        
        r = []
        for n, v in d.items():
            r.append((-1 * v, n))
        heapq.heapify(r)

        res = []
        for j in range(k):
            if r:
                t = heapq.heappop(r)
                res.append(t[1])
        return res

        