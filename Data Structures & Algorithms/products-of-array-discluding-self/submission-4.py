class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_nums = {}
        previous = 1
        for i in range(len(nums)):
            left_nums[i] = previous
            previous *= nums[i]
        
        right_nums = {}
        previous = 1
        for i in range(len(nums)-1, -1, -1):
            right_nums[i] = previous
            previous *= nums[i]
        return [left_nums[i] * right_nums[i] for i in range(len(nums))]