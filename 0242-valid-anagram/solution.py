class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        k=list(set(s))
        d=list(set(t))
        for i in k:
            if s.count(i)!=t.count(i):
                return False
        for i in d:
            if s.count(i)!=t.count(i):
                return False
        return True

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
