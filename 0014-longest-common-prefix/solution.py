class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        c = len(strs[0])

        for i in strs:
            c = min(c, len(i))

        k = ""

        for i in range(c):
            for j in strs:
                if j[i] != strs[0][i]:
                    return k
            k += strs[0][i]

        return k
