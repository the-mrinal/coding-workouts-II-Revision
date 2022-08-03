class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        res = 0
        used = set()
        
        for val,freq in count.items():
            while freq > 0 and freq in used:
                freq -= 1
                res += 1
            
            used.add(freq)
        
        return res