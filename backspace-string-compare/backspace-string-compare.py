class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        A = []
        B = []
        
        for char in s:
            if char is '#':
                if A:
                    A.pop()
            else:
                A.append(char)
        for char in t:
            if char is '#':
                if B:
                    B.pop()
            else:
                B.append(char)
        
        A = ''.join(A)
        B = ''.join(B)
        return A == B
        