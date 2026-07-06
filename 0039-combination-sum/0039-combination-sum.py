class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :type rtype: List[List[int]]
        """
        self.l = []
        
        def back(i, current_sum, s):
            if current_sum == target:
                self.l.append(s)
                return
            
            if current_sum > target or i >= len(candidates):
                return
            back(i, current_sum + candidates[i], s + [candidates[i]])
            back(i + 1, current_sum, s)
            
        back(0, 0, [])
        return self.l


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna