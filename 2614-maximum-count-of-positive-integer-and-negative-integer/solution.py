class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        r=0
        for i in nums:
            if(i>0):
                c+=1
            elif(i<0):
                r+=1
            
        return max(r,c)

