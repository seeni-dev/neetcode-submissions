from math import sqrt
class Solution:
    def distance(self, x2, y2):
        x1, y1 = 0, 0
        # print((x1 - x2)^2, (y1-y2)^2)
        return sqrt((x1 - x2)**2 + (y1 - y2)**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = list(map(lambda p: (self.distance(p[0], p[1]), p), points))
        heapq.heapify(points)
        res = []
        for _ in range(k):
            r = heapq.heappop(points)
            res.append(r[1])
        return res
