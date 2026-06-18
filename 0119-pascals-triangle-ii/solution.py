class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
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
        l=[]
        memo={}
        for i in range(rowIndex+1):
            k=[]
            for j in range(i+1):
                k.append(pascal(i,j,memo))
            l.append(k)
        return l[-1]
        
