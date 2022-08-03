class MinStack:

    def __init__(self):
        self.minarr = []
        

    def push(self, val: int) -> None:
        if not self.minarr:
            self.minarr.append((val,val))
        else:
            self.minarr.append((val,min(val,self.minarr[-1][1])))

    def pop(self) -> None:
        self.minarr.pop()

    def top(self) -> int:
        return self.minarr[-1][0]

    def getMin(self) -> int:
        return self.minarr[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()