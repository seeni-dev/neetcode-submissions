from collections import defaultdict
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = sorted(intervals + [newInterval])

        res = []
        lastInterval = intervals[0]
        for interval in intervals[1:]:
            # print(lastInterval, interval)
            if interval[0] in range(lastInterval[0], lastInterval[1]+1):
                # print("Need to merge")
                lastInterval[1] = max(interval[1], lastInterval[1])
            else:
                res.append(lastInterval)
                lastInterval = interval
        res.append(lastInterval)
        return res