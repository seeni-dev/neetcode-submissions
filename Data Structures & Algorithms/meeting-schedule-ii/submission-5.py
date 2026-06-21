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
        timeline = defaultdict(lambda :{"start": 0, "end": 0})
        for interval in intervals:
            timeline[interval.start]["start"] += 1
            timeline[interval.end]["end"] += 1
        noOfMeetingRooms = 0
        maxNoOfMeetingRooms = 0
        for t in sorted(timeline.keys()):
            noOfMeetingRooms += timeline[t]["start"] - timeline[t]["end"]
            maxNoOfMeetingRooms = max(maxNoOfMeetingRooms, noOfMeetingRooms)
        return maxNoOfMeetingRooms