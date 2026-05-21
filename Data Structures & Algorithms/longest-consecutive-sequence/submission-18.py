import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        heapq.heapify(nums)
        longest_sequence = 0
        previous = None
        current_length = 0
        while nums:
            n = heapq.heappop(nums)
            if n == previous:
                continue
            
            if previous != n - 1:
                current_length = 0
            previous = n
            current_length+=1
            longest_sequence = max(current_length, longest_sequence)

        return longest_sequence