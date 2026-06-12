class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        s=0
        for i in hours:
            if(i>=target):
                s+=1
        return s
        
