class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for num in nums:
            if num in h:
                return True 
            h[num] = True
        return False