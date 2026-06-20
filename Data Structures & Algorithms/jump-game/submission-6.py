class Solution:
    def canJump(self, nums: List[int]) -> bool:
        numsHash = {len(nums)-1: True}
        for i in range(len(nums)-2, -1, -1):
            for jump in range(1, min(len(nums),nums[i]+1)):
                jumpedI = i + jump
                res = False
                if jumpedI >= len(nums) - 1:
                    res = True
                elif jumpedI in numsHash:
                    res = numsHash[jumpedI]
                numsHash[i] = res
                if res:
                    break
            if i not in numsHash:
                numsHash[i] = False
        return numsHash[0]