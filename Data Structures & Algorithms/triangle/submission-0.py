from collections import defaultdict
import sys
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        depth = 0
        currentCost = defaultdict(lambda :sys.maxsize)
        currentCost[0] = triangle[0][0]
        while depth < len(triangle) - 1:
            newCost = defaultdict(lambda :sys.maxsize)
            for i in range(len(triangle[depth])):
                newCost[i] = min(newCost[i], currentCost[i] + triangle[depth+1][i])
                newCost[i+1] = min(newCost[i+1], currentCost[i] + triangle[depth+1][i+1])
            currentCost = newCost
            depth +=1
        return min(currentCost.values())