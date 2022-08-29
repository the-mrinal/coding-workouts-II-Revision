class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        start = 0
        n = len(s)
        maxSize = 0
        freq = defaultdict(int)
        for end in range(n):
            freq[s[end]] += 1
            
            while len(freq.keys()) > 2:
                if freq[s[start]] > 1:
                    freq[s[start]] -= 1
                else:
                    del freq[s[start]]
                start += 1
            
            if len(freq.keys()) <= 2:
                maxSize = max(maxSize,end - start + 1)
        
        return maxSize