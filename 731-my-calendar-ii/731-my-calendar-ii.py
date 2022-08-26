class MyCalendarTwo:

    def __init__(self):
        self.bookMap = defaultdict(int)
        

    def book(self, start: int, end: int) -> bool:
        self.bookMap[start] += 1
        self.bookMap[end] -= 1
        count = 0
        for val in sorted(self.bookMap.keys()):
            count += self.bookMap[val]
            if count == 3:
                self.bookMap[start] -= 1
                self.bookMap[end] += 1
                return False
        return True        
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)