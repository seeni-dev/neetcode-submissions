class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for v in nums:
            if v < 0:
                v *= -1
            index = v - 1
            if nums[index] < 0:
                return v
            nums[index] *=-1
        