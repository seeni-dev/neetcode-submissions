class Solution:
    def reverseBits(self, n: int) -> int:
        r = []
        while n:
            r.append(str(n & 1))
            n = n >> 1
        r = r + ['0' * (32-len(r))]
        return int(''.join(r), 2)
        