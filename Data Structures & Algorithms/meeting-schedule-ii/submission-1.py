"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTimes = [interval.start for interval in intervals]
        endTimes = [interval.end for interval in intervals]
        startTimes.sort()
        endTimes.sort()
        startIndex, endIndex = 0,0
        currentMeetingsCount = 0
        maxMeetingsCount = 0
        while startIndex in range(0,len(startTimes)):
            if startTimes[startIndex] < endTimes[endIndex]:
                currentMeetingsCount+=1
                maxMeetingsCount = max(maxMeetingsCount, currentMeetingsCount)
                startIndex+=1
            else:
                currentMeetingsCount-=1
                endIndex+=1
        return maxMeetingsCount


    