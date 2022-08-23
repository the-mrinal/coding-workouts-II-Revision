class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        st = []
        n = len(temp)
        res = [0]*n
        for i in range(n - 1,-1,-1):
            if st:
                while st and st[-1][0] <= temp[i]:
                    st.pop()
                if st and st[-1][0] > temp[i]:
                    res[i] = st[-1][1] - i
                else:
                    res[i] = 0
            st.append([temp[i],i])
        
        return res
            