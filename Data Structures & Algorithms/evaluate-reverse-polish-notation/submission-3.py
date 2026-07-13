class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def evaluate(token, num1, num2):
            if token == '+':
                return num2 + num1
            if token == '-':
                return num2 - num1
            if token == '*':
                return num2 * num1
            return int(num2 / num1)

        stack = []
        for token in tokens:
            if token in "+*-/":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(evaluate(token, num1, num2))
            else:
                stack.append(int(token))
        return stack.pop()