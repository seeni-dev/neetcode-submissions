class Solution:
    def operate(self, operator, op1, op2):
        if operator == "+":
            return op1 + op2
        elif operator == '-':
            return op1 - op2
        elif operator == '*':
            return op1 * op2
        else:
            return int(op1/op2)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+": 1, "-": 1, "*": 2, "/": 2}
        for token in tokens:
            if token in operators:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(self.operate(token,  op1, op2))   
            else:
                stack.append(int(token))
            # print(stack)
        return stack[-1]