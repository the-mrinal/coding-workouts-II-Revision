class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n1 = len(beginWord)
        n2 = len(endWord)
        
        if n1 != n2 or endWord not in wordList or n1 != len(wordList[0]):
            return 0
        
        all_dict = defaultdict(list)
        
        for w in wordList:
            for i in range(n1):
                currW = w[:i] + "*" + w[i+1:]
                all_dict[currW].append(w)
        
        que = deque()
        que.append([beginWord,1])
        
        visited = set()
        visited.add(beginWord)
        while que:
            currW,level = que.popleft()
            if currW == endWord:
                print(currW,level,que)
                return level
            
            for i in range(n1):
                tempW = currW[:i] + "*" + currW[i+1:]
                for child in all_dict[tempW]:
                    if child not in all_dict:
                        que.append([child,level + 1])
                        visited.add(child)
                all_dict[tempW] = []
            
        
        return 0
       