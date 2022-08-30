class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left = [float('inf') if seats[0] == 0 else 0]
        right = [float('inf') if seats[-1] == 0 else 0]
        n = len(seats)
        print(left,right)
        i = 1
        while i < n:
            if seats[i] == 0:
                left.append(left[i - 1] + 1)
            else:
                left.append(0)
            if seats[n - i - 1] == 0:
                right.append(right[i - 1] + 1)
            else:
                right.append(0)
            i += 1
        right = list(reversed(right))
        res = -1
        ans = -1
        for i  in range(n):
            curr = min(left[i],right[i])
            if res < curr:
                res = curr
                ans = i
        
        return res