class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        k=[]
        for i in range(len(s)):
            if(s[i]=="(" or s[i]=="{" or s[i]=="["):
                k.append(s[i])
            else:
                if not k:
                    return False
                top=k.pop()
                if(s[i]==")" and top!="(") or (s[i]=="}" and top!="{") or (s[i]=="]" and top!="["):
                    return False
        return len(k)==0
