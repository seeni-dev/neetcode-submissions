class Solution:
    def canJump(self, nums: List[int]) -> bool:
        numsHash = {len(nums)-1: True}
        for i in range(len(nums)-2, -1, -1):
            # print(f"At {i}")
            for jump in range(1, nums[i]+1):
                jumpedI = i + jump
                # print(f"Jumped to {jumpedI}")
                res = False
                if jumpedI >= len(nums) - 1:
                    res = True
                elif jumpedI in numsHash:
                    res = numsHash[jumpedI]
                numsHash[i] = res
                if res:
                    # print(f"Jump possible")
                    break
            if i not in numsHash:
                numsHash[i] = False
        return numsHash[0]