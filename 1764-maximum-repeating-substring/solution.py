class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :type rtype: int
        """
        memo = {}
        word_len = len(word)
        seq_len = len(sequence)
        
        def dp(i):
            if i + word_len > seq_len:
                return 0
            if i in memo:
                return memo[i]
            if sequence[i : i + word_len] == word:
                memo[i] = 1 + dp(i + word_len)
            else:
                memo[i] = 0
                
            return memo[i]
        
        max_k = 0
        for i in range(seq_len):
            max_k = max(max_k, dp(i))
            
        return max_k
