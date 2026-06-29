import heapq
from collections  import defaultdict
import sys

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(lambda : {})
        costMap = defaultdict(lambda: sys.maxsize)
        for u,v,t in times:
            graph[u][v] = t

        q = [(0, k,)]
        costMap[k] = 0
        visited = set([k])

        while q:
            currentCost, node = heapq.heappop(q)
            if currentCost > costMap[node]:
                continue
            visited.add(node)
            for neighbour, t in graph[node].items():
                newCost = currentCost + t
                if newCost < costMap[neighbour]:
                    costMap[neighbour] = newCost
                    heapq.heappush(q, (newCost, neighbour, ))
        print(costMap)
        if len(visited) == n:
            return max(costMap.values())
        else:
            return -1