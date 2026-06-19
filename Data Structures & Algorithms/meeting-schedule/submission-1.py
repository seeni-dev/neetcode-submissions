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
        interval = intervals[0]
        for nextInterval in intervals[1:]:
            if nextInterval.start in range(interval.start, interval.end):
                return False
            interval = nextInterval
        return True