class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for _ in s:
            if stack and _ == ']' and stack[-1] == '[':
                stack.pop()
            elif stack and _ == '}' and stack[-1] == '{':
                stack.pop()
            elif stack and _ == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(_)


        return len(stack) == 0