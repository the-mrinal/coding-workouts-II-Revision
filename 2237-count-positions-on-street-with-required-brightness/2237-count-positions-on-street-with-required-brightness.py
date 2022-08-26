class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        brightMap = defaultdict(int)   
    
        for p,r in lights:
            start = max(0,p - r)
            end = min(n-1,p + r)
            brightMap[start] += 1
            brightMap[end + 1] -= 1
        
        bright = [0]*n
        currLight = 0
        for index in range(n):
            if index in brightMap:
                currLight += brightMap[index]
            bright[index] = currLight
        
        
        
        
        count = 0
        for index,reqB in enumerate(requirement):
            if reqB <= bright[index]:
                count += 1
        
        return count