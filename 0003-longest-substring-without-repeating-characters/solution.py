class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0

        max_len = 0
        temp = []  
        left = 0

        for right in range(n):
            char = s[right]

            while char in temp:
                temp.pop(0)

            temp.append(char)
            max_len = max(max_len, len(temp))

        return max_len

