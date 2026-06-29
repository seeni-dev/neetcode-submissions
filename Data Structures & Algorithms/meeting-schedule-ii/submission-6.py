"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import defaultdict
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervalsList = []
        for interval in intervals:
            intervalsList.append((interval.start, 1, ))
            intervalsList.append((interval.end, -1,))
        intervalsList = sorted(intervalsList)
        meetingRooms = 0
        maxMeetingRooms = 0
        for interval in intervalsList:
            meetingRooms += interval[1]
            maxMeetingRooms = max(maxMeetingRooms, meetingRooms)
        return maxMeetingRooms