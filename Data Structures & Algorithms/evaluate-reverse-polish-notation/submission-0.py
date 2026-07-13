class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token in ['+', '-', '*', '/']:
                operand1 = stack.pop()
                operand2 = stack.pop()
                if token == '+':
                    stack.append(operand1+operand2)
                elif token == '-':
                    stack.append(-operand1+operand2)
                elif token == '*':
                    stack.append(operand1*operand2)
                elif token == '/':
                    stack.append(int(operand2/operand1))
            else:
                stack.append(int(token))
            i += 1
        return stack[0]