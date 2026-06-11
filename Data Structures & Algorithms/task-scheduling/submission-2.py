import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasksCount = defaultdict(lambda : 0)
        for t in tasks:
            tasksCount[t] +=1

        waitQ = []
        readyQ = [[tasksCount[i], i] for i in tasksCount.keys()]
        heapq.heapify_max(readyQ)
        t = 0
        while readyQ or waitQ:
            tC = 1
            e = None
            while waitQ and waitQ[0][0] <= t:
                time, tC, e = heapq.heappop(waitQ)
                heapq.heappush_max(readyQ, [-1*tC, e])
            if readyQ:
                tC, e = heapq.heappop_max(readyQ)
                print("Ready", tC, e)
            elif waitQ:
                time, tC, e = heapq.heappop(waitQ)
                tC *= -1
                print("Wait", tC, e)
                t = time
            t += 1
            if tC > 1:
                heapq.heappush(waitQ, [t + n, -1 * (tC - 1), e])
        return t
