class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        arr = []
        
        def findPower(num):
            if num == 1:
                return 0
            if num % 2 == 0:
                return 1 + findPower(num/2)
            else:
                return 1 + findPower(3*num + 1)
        
        for num in range(lo,hi + 1):
            power = findPower(num)
            arr.append([power,num])
        
        arr.sort()
        # print(arr)
        return arr[k-1][1]