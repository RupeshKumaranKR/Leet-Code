class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True
            
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                k1 = s[:left] + s[left+1:]
                if k1 == k1[::-1]:
                    return True
                    
                k2 = s[:right] + s[right+1:]
                if k2 == k2[::-1]:
                    return True
                    
                return False
                
            left += 1
            right -= 1
            
        return False

