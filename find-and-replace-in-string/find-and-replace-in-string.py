class Solution:
    def findReplaceString(self, S: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        for i,s,t in sorted(zip(indices,sources,targets),reverse=True):
            S = S[:i] + t + S[i + len(s):] if S[i:i+len(s)] == s else S
        
        return S