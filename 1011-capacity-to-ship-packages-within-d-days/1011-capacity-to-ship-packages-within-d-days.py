'''
left = max(weights)
right = sum(weights)

def condition(shipC):
    currWeight = 0
    currDay = 1
    for i in range(len(weights)):
        currWeight += weights[i]
        if currWeight > shipC:
            currday += 1
            currWeight = weight[i]
        if currDay > days:
            return False
    
    return True

'''

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        def condition(shipC):
            currWeight = 0
            currDay = 1
            for i in range(len(weights)):
                currWeight += weights[i]
                if currWeight > shipC:
                    currDay += 1
                    currWeight = weights[i]
                if currDay > days:
                    return False
            return True
        
        while left < right:
            mid = left + (right - left) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return left