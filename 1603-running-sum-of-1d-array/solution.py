class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=0
        l=[]
        for i in nums:
            s+=i
            l.append(s)
        return l
