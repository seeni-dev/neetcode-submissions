class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        isNegative = x < 0
        x = abs(x)
        while x:
            c = x % 10
            r = r * 10 + c
            x = x//10
        res = r * (-1 if isNegative else 1)
        MIN, MAX = -2**31, 2**31 - 1
        print(res, res in range(MIN, MAX+1))
        return res if res in range(MIN, MAX+1) else 0
        