class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        l=[]
        for i in accounts:
            s=sum(i)
            l.append(s)
        s=max(l)
        return s

        
