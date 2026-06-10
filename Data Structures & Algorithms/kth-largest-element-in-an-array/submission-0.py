import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        while k > 1 and nums:
            heapq.heappop_max(nums)
            k -=1
        if k and nums:
            return heapq.heappop_max(nums)
        
        