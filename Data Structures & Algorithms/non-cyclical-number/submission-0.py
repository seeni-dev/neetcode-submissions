class Solution:
    def isHappy(self, n: int) -> bool:
        h = {}
        while n not in h:
            h[n] = True
            s = 0
            while n:
                b = n % 10
                s += b * b
                n = n // 10
            # print(s)
            n = s
        return n ==1
        