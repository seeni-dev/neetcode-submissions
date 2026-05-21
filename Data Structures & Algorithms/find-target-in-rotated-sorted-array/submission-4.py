class Solution:
    def bs(self, nums, left, right, target):
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle -1
        return -1
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
        pivot = left
        res = self.bs(nums, pivot, len(nums) - 1, target)
        if res == -1 and pivot != 0:
            res = self.bs(nums, 0, pivot, target)
        return res