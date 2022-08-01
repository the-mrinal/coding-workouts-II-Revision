class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        "lee(t(c)o)de)"
        stack = []
        if s[index] == '('
            stack.push i
        elif ')':
            if not stack:
                to_remove.push(i)
            else:
                stack.pop - this will help openin brackets.
        
        while stack:
            to_remove(stack.push)
        '''
        def sanitise():
            n = len(s)
            st = []
            to_remove = []
            new_s = ""
            for i in range(n):
                if s[i] == '(':
                    st.append(i)
                elif s[i] == ')':
                    if st:
                        st.pop()
                    else:
                        to_remove.append(i)
            while st:
                to_remove.append(st.pop())
            
            for i in range(n):
                if i in to_remove:
                    continue
                new_s += s[i]
            return new_s
        
        return sanitise()