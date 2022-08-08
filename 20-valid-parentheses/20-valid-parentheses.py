class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for elem in s:
            if elem in ['[','{','(']:
                 stack.append(elem)
            else:
                if stack:
                    curr = stack.pop()
                    if not ((curr == '[' and elem == ']') or (curr == '(' and elem == ')') or (curr == '{' and elem == '}')): 
                        return False
                else:
                    return False
        if stack:
            return False
        return True