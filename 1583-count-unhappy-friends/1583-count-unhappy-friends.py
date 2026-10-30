class Solution:
    def unhappyFriends(self, n: int, preferences: list[list[int]], pairs: list[list[int]]) -> int:
        
        row,col =len(preferences),len(preferences[0])
        rank={}

        for i in range(n):
            rank[i]={}
            for prefix_index,friend in enumerate(preferences[i]):
                rank[i][friend]=prefix_index
        

        paired_with={}
        for u,v in pairs:
            paired_with[u]=v
            paired_with[v]=u
        
        unhappy=0
        for x in range(n):
            y = paired_with[x]
            for u in preferences[x]:
                if u == y:
                    break
                v=paired_with[u]
                if rank[u][x] < rank[u][v]:
                    unhappy+=1
                    break
        return unhappy
