class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = []
        lastInterval = intervals[0]
        for interval in intervals[1:]:
            if lastInterval is None:
                lastInterval = interval
            elif interval[0] in range(lastInterval[0], lastInterval[1]+1):
                lastInterval = [
                    min(interval[0], lastInterval[0]),
                    max(interval[1], lastInterval[1])
                ]
            else:
                res.append(lastInterval)
                lastInterval = interval
        if lastInterval:
            res.append(lastInterval)
        return res