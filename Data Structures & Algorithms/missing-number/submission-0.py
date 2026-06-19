class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = 0
        for n in range(len(nums)+1):
            x = x ^ n
        for n in nums:
            x = x ^ n
        return x
        