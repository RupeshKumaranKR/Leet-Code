class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        m=[0]*(n+1)
        m[1]=1
        m[2]=2
        for i in range(3,n+1):
            m[i]=m[i-2]+m[i-1]
        return m[n]
        
