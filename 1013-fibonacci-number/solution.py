class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo={}
        def fibo(n,memo):
            if n<=0:
                return 0
            if n==1 or n==2:
                return 1
            if n in memo:
                return memo[n]
            memo[n]=fibo(n-1,memo)+fibo(n-2,memo)
            return memo[n]
        return fibo(n,memo)
        
