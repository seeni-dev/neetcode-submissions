"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        timeline = {}
        maxT = 0
        for interval in intervals:
            start,end = interval.start, interval.end
            if start not in timeline:
                timeline[start] = 0
            timeline[start] +=1
            if end not in timeline:
                timeline[end] = 0
            timeline[end]-=1
            maxT = max(end, maxT)
        maxMeetings = 0
        currentMeetingCount = 0
        for i in range(maxT+1):
            if i in timeline:
                currentMeetingCount += timeline[i]
                maxMeetings = max(maxMeetings, currentMeetingCount)
        return maxMeetings

    