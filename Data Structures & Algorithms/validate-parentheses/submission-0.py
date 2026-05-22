class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        for c in s:
            if c in paren:
                stack.append(c)
            else:
                # print(stack)
                if not(stack and paren[stack.pop()] == c):
                    return False
        return len(stack) ==0

        