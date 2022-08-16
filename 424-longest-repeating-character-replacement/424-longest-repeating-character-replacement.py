class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        window_set = {}
        maxLen = float('-inf')
        maxRepeating = 0
        n = len(s)
        
        for end in range(n):
            if s[end] in window_set:
                window_set[s[end]] += 1
            else:
                window_set[s[end]] = 1
            
            maxRepeating = max(maxRepeating,window_set[s[end]])
            
            while end - start + 1 - maxRepeating > k:
                window_set[s[start]] -= 1
                start += 1
            maxLen = max(maxLen,end - start + 1)
        
        return maxLen