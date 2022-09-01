class Solution:
    def freqGen(self,arr) -> dict:
        hashMap = {}
        for s in arr:
            if s not in hashMap:
                hashMap[s] = 1
                continue
            hashMap[s] += 1
        return hashMap
    def isAnagram(self, t: str, s: str) -> bool:
        if len(s) > len(t):
            return False
        hashMap = self.freqGen(t)
        for char in s:
            if char not in hashMap or hashMap[char] <= 0:
                return False
            hashMap[char] -= 1
        
        setMap = set(hashMap.values())
        return 0 in setMap and len(setMap) == 1