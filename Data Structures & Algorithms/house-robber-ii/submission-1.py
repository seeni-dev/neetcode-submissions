from collections import defaultdict
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp1 = defaultdict(lambda :0)
        for i in range(1, len(nums)):
            n = nums[i]
            dp1[i] = max(
                dp1[i-2] + nums[i],
                dp1[i-1]
            )
        
        dp2 = defaultdict(lambda :0)
        for i in range(len(nums)-1):
            n = nums[i]
            dp2[i] = max(
                dp2[i-2] + nums[i],
                dp2[i-1]
            )
        return max(dp1[len(nums)-1], dp2[len(nums)-2])
            