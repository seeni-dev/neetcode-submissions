class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                lower_tmp = stack.pop()
                res[lower_tmp] = i - lower_tmp
            stack.append(i)
        return res