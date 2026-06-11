class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=list(set(nums))
        if len(n)==len(nums):
            return False
        else:
            return True
        
