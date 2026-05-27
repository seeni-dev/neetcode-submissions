class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = -1
        while left <= right:
            speed = (left + right) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / speed)        
            if time > h:
                left = speed + 1
            elif time <= h:
                ans = speed
                right = speed - 1
        return ans