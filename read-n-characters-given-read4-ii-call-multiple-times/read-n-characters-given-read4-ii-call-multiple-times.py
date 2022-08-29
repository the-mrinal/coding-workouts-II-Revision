# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    
    def __init__(self):
        self.que = deque()
    
    
    def read(self, buf: List[str], n: int) -> int:
        
        index = 0
        
        while index < n:
            if self.que:
                buf[index] = self.que.popleft()
                index += 1
            else:
                buf4 = [""]*4
                count = read4(buf4)
                if count == 0:
                    break
                self.que.extend(buf4[:count])
        return index
     