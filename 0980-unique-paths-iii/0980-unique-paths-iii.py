class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.count=0
        r=len(grid)
        c=len(grid[0])
        k=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    sx,sy=i,j
                if grid[i][j]==2:
                    dx,dy=i,j
                if grid[i][j]==0:
                    k+=1
        def path(i,j,s):
            if i<0 or i>r-1 or j<0 or j>c-1 or s[i][j]==1 or grid[i][j]==-1:
                return
            if (i==dx and j==dy) and sum(row.count(1) for row in s)==k+1:
                self.count+=1
                return
            s[i][j]=1
            path(i+1,j,s)
            path(i,j+1,s)
            path(i-1,j,s)
            path(i,j-1,s)
            s[i][j]=0
        s=[[0]*c for _ in range(r)]
        path(sx,sy,s)
        return self.count

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna