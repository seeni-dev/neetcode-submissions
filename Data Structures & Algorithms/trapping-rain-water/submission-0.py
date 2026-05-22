class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        trapped = 0
        while left < right:
            if height[left] < height[right]:
                current = left + 1
                while left < right and height[current] < height[left]:
                    trapped += height[left] - height[current]
                    current +=1
                left = current
            else:
                current = right - 1
                while left < right and height[current] < height[right]:
                    trapped += height[right] - height[current]
                    current -=1
                right = current
        return trapped
            