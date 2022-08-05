class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}
        start = 0
        n = len(nums)
        for end in range(n):
            if end > k:
                del hashMap[nums[start]]
                start += 1
            if nums[end] not in hashMap:
                hashMap[nums[end]] = end
            else:
                return True
        
        return False