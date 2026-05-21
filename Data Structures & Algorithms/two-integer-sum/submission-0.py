class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            r = target - n
            if r in d:
                return [d[r], i]
            d[n] = i
        return None
        