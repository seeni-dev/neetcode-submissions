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
        timeline = defaultdict(dict)
        for interval in intervals:
            start, end = interval.start, interval.end
            timeline[start]["start"] = timeline[start].get("start", 0) + 1
            timeline[end]["end"] = timeline[end].get("end",0) + 1
        
        timestamps = sorted(timeline.keys())
        meetingRooms = 0
        maxMeetingRooms = 0
        for timestamp in timestamps:
            meetingRooms += timeline[timestamp].get("start", 0)
            meetingRooms -=  timeline[timestamp].get("end", 0)
            print(f" At {timestamp} leaving with #{meetingRooms}")
            maxMeetingRooms = max(maxMeetingRooms, meetingRooms)
            # print(f" At {timestamp} found #{meetingRooms}")

        return maxMeetingRooms