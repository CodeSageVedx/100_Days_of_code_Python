# Unique Paths 2
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dfsStack = []


        direction = [(1,0) , (0,1) ]
  
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0]:
            return 0


        memo = [[0 for _ in range(n)] for _ in range(m)]   

        # inititalise the memo for the dest
        memo[m-1][n-1]=1


        def recurDFS(i,j):
            
            if obstacleGrid[i][j]==1:
                return 0

            if memo[i][j] !=0:
                return memo[i][j]

            for x,y in direction:
                # print(x,y)
                dx = i+x
                dy = j+y
                

                if 0<=dx<m and 0<=dy<n  :
                    # print(">",dx,dy)
                   memo[i][j] += recurDFS(dx,dy)

            return memo[i][j]

        recurDFS(0,0)
        for i in range(m):
            print(memo[i])
        return memo[0][0]