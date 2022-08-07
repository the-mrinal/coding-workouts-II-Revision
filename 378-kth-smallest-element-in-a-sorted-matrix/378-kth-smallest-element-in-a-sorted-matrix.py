class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxHeap = []
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m*n):
            x = i // n
            y = i % n
            if i < k:
                heappush(maxHeap,-matrix[x][y])
            else:
                if matrix[x][y] < -maxHeap[0]:
                    heappop(maxHeap)
                    heappush(maxHeap,-matrix[x][y])
        return -maxHeap[0]