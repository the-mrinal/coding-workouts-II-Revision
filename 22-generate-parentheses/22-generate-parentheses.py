class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def generate(S,left,right):
            nonlocal ans
            if left + right == n*2:
                ans.append(''.join(S))
                return
            if left < n:
                generate(S + ['('],left + 1,right)
            
            if right < left:
                generate(S+[')'],left ,right + 1)
            
            return 
        generate([],0,0)
        
        return ans