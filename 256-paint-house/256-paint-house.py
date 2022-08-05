class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        cache = {}
        def minCostDP(index,prevC):
            nonlocal cache
            if index == n:
                return 0
            
            key = (index,prevC)
            if prevC == -1:
                cache[(index,prevC)] = min(costs[index][0] + minCostDP(index +1,0),costs[index][1] + minCostDP(index +1,1),costs[index][2] + minCostDP(index +1,2))
                return cache[(index,prevC)]
            
            
            if key not in cache:
                ans1 = 0
                ans2 = 0
                if prevC == 0:
                    ans1 = costs[index][1] + minCostDP(index +1,1)
                    ans2 = costs[index][2] + minCostDP(index+1,2)
                elif prevC == 1:
                    ans1 = costs[index][0] + minCostDP(index +1,0)
                    ans2 = costs[index][2] + minCostDP(index+1,2)
                else:
                    ans1 = costs[index][1] + minCostDP(index +1,1)
                    ans2 = costs[index][0] + minCostDP(index+1,0)
                cache[key] = min(ans1,ans2)
            
            return cache[key]
        
        minCostDP(0,-1)
        return cache[(0,-1)]