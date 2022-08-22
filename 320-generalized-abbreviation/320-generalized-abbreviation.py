class Substring:
    
    def __init__(self,s=[],start=0,count=0):
        self.s = s
        self.start = start
        self.count = count
    
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
        result = []
        n = len(word)
        
        que = deque()
        que.append(Substring())
        
        while que:
            curr = que.popleft()
            
            if curr.start == n:
                if curr.count != 0:
                    curr.s.append(str(curr.count))
                result.append(''.join(curr.s))
            else:
                que.append(Substring(list(curr.s),curr.start + 1,curr.count+1))
                
                if curr.count != 0:
                    curr.s.append(str(curr.count))
                
                new_word = list(curr.s)
                new_word.append(word[curr.start])
                que.append(Substring(new_word,curr.start +1,0))
        
        return result