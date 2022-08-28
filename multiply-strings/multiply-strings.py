class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = []
        if num1 == "0" or num2 == "0":
            return "0"
        def addition(A,B):
            res = []
            aSize = len(A)
            bSize = len(B)
            size = max(aSize,bSize)
            carry = 0
            for i in range(size):
                aVal = int(A[i]) if i < aSize else 0
                bVal = int(B[i]) if i < bSize else 0
                curr = aVal + bVal + carry
                carry = curr // 10
                curr = curr % 10
                res.append(str(curr))
            if carry > 0:
                res.append(str(carry))
            return res
            
            
            
            
        count = 0
        totalSum = []
        currSum = []
        
        for i in reversed(num1):
            carry = 0
            for j in reversed(num2):
                currP = (int(i)*int(j))+ carry
                carry = currP // 10
                currP = currP % 10
                currSum.append(str(currP))
            buffer = [0] * count
            
            if carry > 0:
                currSum.append(str(carry))
            currSum = buffer + currSum
            totalSum = addition(totalSum,currSum)
            count += 1
            currSum = []
        return ''.join(totalSum[::-1])