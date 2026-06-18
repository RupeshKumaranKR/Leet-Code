class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def pascal(r,c,memo):
            if(c==0 or r==c):
                return 1
            if (r,c) in memo:
                return memo[(r,c)]
            left=pascal(r-1,c-1,memo)
            right=pascal(r-1,c,memo)
            t=left+right
            memo[(r,c)]=t
            return t
        c=[]
        memo={}
        for i in range(numRows):
            r=[]
            for j in range(i+1):
                r.append(pascal(i,j,memo))
            c.append(r)
        return c

        
        
