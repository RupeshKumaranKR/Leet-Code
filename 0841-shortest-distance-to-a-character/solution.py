class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        n = len(s)
        ans = [0] * n
        
        pos = -float('inf')
        for i in range(n):
            if s[i] == c:
                pos = i
            ans[i] = i - pos
            
        pos = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                pos = i
            ans[i] = min(ans[i], pos - i)
            
        return ans

