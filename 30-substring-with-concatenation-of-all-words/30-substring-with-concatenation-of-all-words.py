class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        n = len(s)
        word_len = len(words[0])
        n_word = len(words)

        total_len = n_word * word_len


        words.sort()	

        def validate(start,end):
            word_list = s[start:end + 1]
            word_list = [word_list[i:i+word_len] for i in range(0,total_len,word_len)]
            word_list.sort()

            for index in range(n_word):
                if word_list[index] != words[index]:
                    return False

            return True




        start = 0
        ans = []
        for end in range(n):
            if end - start + 1 == total_len:
                if validate(start,end):
                    ans.append(start)
                start += 1

        return ans
