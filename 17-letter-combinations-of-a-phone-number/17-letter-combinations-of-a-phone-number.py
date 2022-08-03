class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numberMap = {
            2:['a','b','c'],
            3:['d','e','f'],
            4:['g','h','i'],
            5:['j','k','l'],
            6:['m','n','o'],
            7:['p','q','r','s'],
            8:['t','u','v'],
            9:['w','x','y','z']
        }
        
        def helper(number):
            if number == "":
                return []
            if len(number) == 1:
                return numberMap[int(number)]
            
            ans = helper(number[1:])
            currAns = []
            for n in numberMap[int(number[0])]:
                for c in ans:
                    currAns.append(n + c)
            return currAns
        
        
        return helper(digits)