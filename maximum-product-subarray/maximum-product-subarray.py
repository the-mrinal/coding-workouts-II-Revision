class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = 1
        minProd = 1
        maxSoFar = float('-inf')
        for n in nums:
            temp = max(n,maxProd*n,minProd*n)
            minProd = min(n,maxProd*n,minProd*n)
            maxProd = temp
            maxSoFar = max(maxProd,maxSoFar)
        
        return maxSoFar