class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxP = 0
        while left < right:
            area = abs(right- left) * min(height[left], height[right])
            print(left, right, height[left], height[right], area)
            if height[left] < height[right]:
                left +=1
            else:
                right -=1
            maxP = max(area, maxP)
        return maxP