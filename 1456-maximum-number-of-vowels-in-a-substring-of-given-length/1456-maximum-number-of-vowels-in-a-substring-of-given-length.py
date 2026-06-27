class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = set('aeiou')
        current_vowels = 0
        max_vowels = 0
        
        for i in range(len(s)):
            
            if s[i] in vowels:
                current_vowels += 1
                
            
            if i >= k:
                if s[i - k] in vowels:
                    current_vowels -= 1
            
            
            max_vowels = max(max_vowels, current_vowels)
            
        return max_vowels


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna