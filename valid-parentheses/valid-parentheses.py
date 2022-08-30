class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ["(","{","["]:
                stack.append(char)
            elif char == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif char == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif char == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        
        return True if len(stack) == 0 else False