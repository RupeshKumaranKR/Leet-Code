class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        memo = {0: 0} 
        
        def dp(i):
            if i in memo:
                return memo[i]
            memo[i] = dp(i >> 1) + (i & 1)
            return memo[i]

        ans = []
        for i in range(n + 1):
            ans.append(dp(i))
            
        return ans
