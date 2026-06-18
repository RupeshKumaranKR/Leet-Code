class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo={}
        def tf(n,memo):
            if n<=0:
                return 0
            if n==1 or n==2:
                return 1
            if n in memo:
                return memo[n]
            memo[n]=tf(n-1,memo)+tf(n-2,memo)+tf(n-3,memo)
            return memo[n]
        return tf(n,memo)
            
        
