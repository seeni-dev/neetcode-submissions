"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals = sorted(intervals, key = lambda x: [x.start, x.end])
        lastInterval = intervals[0]
        for interval in intervals[1:]:
            if interval.start in range(lastInterval.start, lastInterval.end):
                return False
            lastInterval = interval
        return True