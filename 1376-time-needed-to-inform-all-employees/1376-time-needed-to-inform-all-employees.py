class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        adjMap =  [[] for i in range(n)]
        for i in range(n):
            if manager[i] != -1:
                adjMap[manager[i]].append(i)
        
        def dfs(iD):
            return max([dfs(i) for i in adjMap[iD]] or [0]) + informTime[iD]
        
        return dfs(headID)
    
    
#     class Solution:
#      def numOfMinutes(self, n, headID, manager, informTime):
#         children = [[] for i in range(n)]
#         for i, m in enumerate(manager):
#             print(i,m)
#             if m >= 0: children[m].append(i)

#         def dfs(i):
#             return max([dfs(j) for j in children[i]] or [0]) + informTime[i]
#         return dfs(headID)
