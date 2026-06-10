import heapq

class MedianFinder:

    def __init__(self):
        self.leftHeap = []
        self.rightHeap = []

    def addNum(self, num: int) -> None:
        if self.leftHeap and num > self.leftHeap[0]:
            heapq.heappush(self.rightHeap, num)
        elif self.rightHeap and num < self.rightHeap[0]:
            heapq.heappush_max(self.leftHeap, num)
        else:
            heapq.heappush_max(self.leftHeap, num)
        if abs(len(self.leftHeap) - len(self.rightHeap)) > 1:
            if len(self.leftHeap) > len(self.rightHeap):
                heapq.heappush(self.rightHeap, heapq.heappop_max(self.leftHeap))
            else:
                heapq.heappush_max(self.leftHeap, heapq.heappop(self.rightHeap))


    def findMedian(self) -> float:
        if len(self.leftHeap) == len(self.rightHeap):
            return (self.leftHeap[0] + self.rightHeap[0]) /2
        elif len(self.leftHeap) > len(self.rightHeap):
            return self.leftHeap[0]
        else:
            return self.rightHeap[0] 
        
        