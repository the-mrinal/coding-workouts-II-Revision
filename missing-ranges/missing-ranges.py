class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums:
            if lower == upper:
                return [f'{lower}']
            return [f'{lower}->{upper}']
        
        if nums[0] != lower:
            nums = [lower - 1] + nums
        if nums[-1] != upper:
            nums = nums + [upper + 1]
        
        res = []
        n = len(nums)
        for i in range(1,n):
            curr = nums[i]
            prev = nums[i - 1]
            
            if abs(curr - prev) > 1:
                left = prev + 1
                right = curr - 1
                if left == right:
                    res.append(str(left))
                else:
                    temp = f'{left}->{right}'
                    res.append(temp)
        
        return res
                