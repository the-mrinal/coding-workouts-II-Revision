class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        
        def findDist(x,y):
            return math.sqrt(x**2 + y**2)
        for x,y in points:
            if len(maxHeap) < k:
                heappush(maxHeap,[-findDist(x,y),x,y])
            else:
                currD = findDist(x,y)
                if -maxHeap[0][0] > currD:
                    heappop(maxHeap)
                    heappush(maxHeap,[-currD,x,y])
        
        ans = []
        # print(maxHeap)
        for d,x,y in maxHeap:
            ans.append([x,y])
        
        return ans