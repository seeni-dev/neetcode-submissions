class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        gasAvailable = 0
        start = 0
        for i in range(len(gas)):
            g = gas[i]
            c = cost[i]
            gasAvailable += g
            gasAvailable -= c
            if gasAvailable < 0:
                start = i + 1
                gasAvailable = 0
        return start
