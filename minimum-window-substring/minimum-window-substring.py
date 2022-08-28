class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = Counter(t)
        start = 0
        minSize = float('inf')
        minWindow = ""
        n = len(s)
        
        def valid_window(nums):
            for val in nums:
                if val > 0:
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

                if end - start + 1 < minSize:
                    minSize = end - start + 1
                    minWindow = s[start:end + 1]
        
        
        return minWindow
        