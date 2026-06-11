class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=len(nums)
        l=[]
        for i in nums:
            if i!=0:
                l.append(i)
        m=len(l)
        c=k-m
        for i in range(c):
            g=0
            l.append(g)
        for i in range(k):
            nums[i]=l[i]


        
