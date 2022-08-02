class Solution:
    def maxScore(self, cards: List[int], k: int) -> int:
        currSum = sum(cards[:k])
        maxSum = currSum
        left = k - 1
        right = len(cards) - 1
        while left >= 0 and right >= len(cards) - k:
            currSum  -= cards[left]
            left -= 1
            currSum += cards[right]
            right -= 1
            maxSum = max(maxSum,currSum)
        return maxSum