class Solution(object):
    def findAnagrams(self, s, p):
        
        k = [0] * 26
        g = [0] * 26
        h = []
        
        if len(p) > len(s): 
            return h
            
        for i in p: 
            k[ord(i)-97] += 1
            
        for c in range(len(p)): 
            g[ord(s[c])-97] += 1
            
        if g == k: 
            h.append(0) 
            
        
        for c in range(len(p), len(s)):
            g[ord(s[c-len(p)])-97] -= 1 
            g[ord(s[c])-97] += 1        
            
            if g == k: 
                h.append(c - len(p) + 1) 
                
        return h


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna