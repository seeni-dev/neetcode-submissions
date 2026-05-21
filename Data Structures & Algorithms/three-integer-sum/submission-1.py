class Solution:
    def twoSum(self, nums: List[int], target, i) -> List[int]:
        mem = {}
        res = []
        for j, jv in enumerate(nums[i:]):
            r = target - jv
            if r in mem:
                res.append([r, jv])
            mem[jv] = True
        return res
            
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = {}
        for i, n in enumerate(nums):
            tuples = self.twoSum(nums, 0-n, i+1)
            for t in tuples:
                t = [n] + t
                r[tuple(sorted(t))] = True
        return list(map(list, list(r.keys())))
        