class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(1<<len(nums)):
            r = [
                nums[j]
                for j in range(len(nums))
                if (1 << j) & i 
            ]
            res.append(r)
        return res
        