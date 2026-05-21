class Solution:
    def isPalindrome(self, s: str) -> bool:
        mod_s = [c.lower() for c in s]
        s = list(filter(
            lambda x: ord(x) in range(ord('a'), ord('z')+1) or ord(x) in range(ord('0'), ord('9')+1),
            mod_s))
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left +=1
            right -=1
        return True