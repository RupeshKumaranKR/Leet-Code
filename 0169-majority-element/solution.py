class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=list(set(nums))
        k=0
        ind=0
        for i,v in enumerate(s):
            if nums.count(v)>k:
                k=nums.count(v)
                ind=i
        return s[ind]



