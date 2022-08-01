class Solution:
    def maxSumDivThree(self,nums):

        zero ,one,two = 0,0,0

        for num in nums:
            options = [num + zero,num + one, num+two]
            for opt in options:
                if opt % 3 == 0:
                    zero = max(zero,opt)
                elif opt % 3 == 1:
                    one = max(one,opt)
                else:
                    two = max(two,opt)
        
        return zero