class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=0
        b=0
        zer0=0
        for i in range(len(nums)):
            if nums[i]==0:
                zer0+=1
            while(zer0>k):
                if nums[l]==0:
                    zer0-=1
                l+=1
            b=max(b,i-l+1)
        return b
            

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna