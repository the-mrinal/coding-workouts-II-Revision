class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxLen = 0
        currSet = {}
        n = len(s)
        if n <= 1:
            return n
        for end in range(n):
            if s[end] not in currSet:
                currSet[s[end]] = end
            else:
                maxLen = max(maxLen,end - start)
                temp = start
                start = currSet[s[end]] + 1
                while temp < start:
                    del currSet[s[temp]]
                    temp += 1
                currSet[s[end]] = end
        maxLen = max(maxLen,end - start + 1)
        return maxLen