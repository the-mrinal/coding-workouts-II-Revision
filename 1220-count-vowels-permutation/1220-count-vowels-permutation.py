class Solution:
    def countVowelPermutation(self, n: int) -> int:

        def isValid(lastWord,currWord):
            if lastWord == "":
                return True
            elif lastWord == 'a' and currWord == 'e':
                return True
            elif lastWord == 'e' and (currWord == 'a' or currWord == 'i'):
                return True
            elif lastWord == 'i' and (currWord in ['a','e','o','u']):
                return True
            elif lastWord == 'o' and (currWord == 'i' or currWord == 'u'):
                return True
            elif lastWord == 'u' and currWord == 'a':
                return True
            return False

        # (i,lastWord)
        dp = {}
        MOD = (10**9) + 7
        def dfs(i,lastWord):
            key = (i,lastWord)
            if i == n:
                return 1

            
            if key not in dp:
                # iterate over 5 vowels:
                dp[key] = 0
                for vowel in ['a','e','i','o','u']:
                    if isValid(lastWord,vowel):
                        dp[key] = (dp[key] + dfs(i+1,vowel))%MOD

            return dp[key]
        ans = dfs(0,"")
        return ans
