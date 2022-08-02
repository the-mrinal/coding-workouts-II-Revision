class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        arr = []
        cache = defaultdict(int)
        def findPower(num):
            if num in cache:
                return cache[num]
            if num == 1:
                return 0
            if num % 2 == 0:
                cache[num] = 1 + findPower(num/2)
            else:
                cache[num] = 1 + findPower(3*num + 1)
            
            return cache[num]
        
        for num in range(lo,hi + 1):
            power = findPower(num)
            arr.append([power,num])
        
        arr.sort()
        # print(arr)
        return arr[k-1][1]