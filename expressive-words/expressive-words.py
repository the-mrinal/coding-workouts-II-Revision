class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def convertIntoExp(curr):
            new_s = ""
            n = len(curr)
            i = 0
            while i < n:
                new_s += curr[i]
                j = i + 1
                while j < n and curr[i] == curr[j]:
                    j += 1
                
                new_s += str(j - i)
                i = j
            return new_s
            
        s = convertIntoExp(s)
        len_s = len(s)
        count = 0
        for w in words:
            temp = convertIntoExp(w)
            flag = True
            if len(temp) == len_s:
                for i in range(0,len_s,2):
                    if s[i] == temp[i]:
                        if s[i + 1] < temp[i + 1]:
                            flag = False
                            break
                        elif s[i + 1] > temp[i + 1] and int(s[i + 1]) < 3:
                            flag = False
                            break
                    else:
                        flag = False
                        break
                if flag:
                    count += 1
        
        return count
                
                
                