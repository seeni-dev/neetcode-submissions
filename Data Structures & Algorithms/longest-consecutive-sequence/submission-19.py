# [2,20,4,10,3,4,5]
# [2,3,4,4,5,10,20]

import heapq
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        countHash = defaultdict(lambda :0)
        maxLength = 0
        for n in nums:
            countHash[n] +=1
        nums = list(set(nums))
        heapq.heapify(nums)

        while nums:
            r = []
            e = heapq.heappop(nums)
            r.append(e)
            while nums and e + 1 == nums[0]:
                e = heapq.heappop(nums)
                r.append(e)
            maxLength = max(maxLength, len(r))
            for e in r:
                countHash[e] -=1
                if countHash[e] > 0:
                    heapq.heappush(nums, e)
        return maxLength

