class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = None
        currentSum = 0
        for i, e in enumerate(nums):
            currentSum += e
            if maxSum is None or maxSum < currentSum:
                maxSum = currentSum
            if currentSum < 0:
                currentSum = 0
        return maxSum
        