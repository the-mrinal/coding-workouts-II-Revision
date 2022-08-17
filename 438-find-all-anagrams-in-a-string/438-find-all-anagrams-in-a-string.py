class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start = 0
        freq = Counter(p)
        
        n = len(s)
        count = []
        for end in range(n):
            if s[end] in freq:
                freq[s[end]] -= 1
            
            if end - start + 1 > len(p):
                if s[start] in freq:
                    freq[s[start]] += 1
                start += 1
            if not any(freq.values()):
                count.append(start)
        return count