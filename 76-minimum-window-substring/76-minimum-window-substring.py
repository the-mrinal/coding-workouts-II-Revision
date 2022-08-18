class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = Counter(t)
        start = 0
        window_s = ""
        minValidWindow = float('inf')
        n = len(s)
        
        
        def valid_window(nums):
            for n in nums:
                if n > 0:
                    return False
            return True
        
        for end in range(n):
            if s[end] in freq:
                freq[s[end]] -= 1
            
            if valid_window(freq.values()):
                while valid_window(freq.values()):
                    if s[start] in freq:
                        freq[s[start]] += 1
                    start += 1
                if not valid_window(freq.values()):
                    start -= 1
                    if s[start] in freq:
                        freq[s[start]] -= 1
                if minValidWindow > end - start + 1:
                    minValidWindow = end- start + 1
                    window_s = s[start:end + 1]
                
        return window_s