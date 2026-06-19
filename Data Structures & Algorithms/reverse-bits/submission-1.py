class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        b = 0
        while n:
            r = (r << 1) | n & 1
            n = n >> 1
            b+=1
        while b < 32:
            r = r << 1
            b +=1
        return r
        