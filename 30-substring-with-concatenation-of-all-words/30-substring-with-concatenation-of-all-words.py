class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words.sort()
        k = len(words)
        k_word = len(words[0])
        total_len = k_word * k
        def validate(start,end):
            curr_words = s[start:end+1]
            curr_word_list = [curr_words[i:i + k_word] for i in range(0,total_len,k_word)]
            curr_word_list.sort()
            # print(curr_word_list,curr_words)
            for i in range(k):
                if words[i] != curr_word_list[i]:
                    return False
            
            return True
        result = []
        start = 0
        for i in range(len(s)):
            if i - start + 1 == total_len:
                if validate(start,i):
                    result.append(start)
                start += 1
        
        return result