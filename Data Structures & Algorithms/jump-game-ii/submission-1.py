class Solution:
    def jump(self, nums: List[int]) -> int:
        q = set([0])
        r = 0
        visited = set()
        while q and len(nums)-1 not in q:
            nq = set()
            for e in q:
                visited.add(e)
                for i in range(1, nums[e]+1):
                    j = e + i
                    if j not in visited:
                        nq.add(j)
            q = nq
            if nq:
                r +=1 
        if len(nums)-1 in q:
            return r
        else:
            return -1