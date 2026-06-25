class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = {}
        window_sum = 0
        max_sum = -float('inf')  

        for i in range(len(nums)):
            window_sum += nums[i]
            freq[nums[i]] = freq.get(nums[i], 0) + 1
            
            if i >= k:
                outgoing = nums[i - k]
                window_sum -= outgoing
                freq[outgoing] -= 1
                if freq[outgoing] == 0:
                    del freq[outgoing]
            
            if i >= k - 1 and len(freq) == k:
                max_sum = max(max_sum, window_sum)
                
        return max_sum if max_sum != -float('inf') else 0


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna