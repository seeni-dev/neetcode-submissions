class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = [intervals[0]]
        for interval in intervals[1:]:
            lastInterval = res[-1]
            if interval[0] in range(lastInterval[0], lastInterval[1]+1):
                res[-1] = [
                    min(interval[0], lastInterval[0]),
                    max(interval[1], lastInterval[1])
                ]
            else:
                res.append(interval)
        return res