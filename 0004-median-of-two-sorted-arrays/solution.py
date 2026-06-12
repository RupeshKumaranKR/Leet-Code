class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a=nums1+nums2
        a=sorted(a)
        k=len(a)
        s=0
        if(k%2==0):
            s=(float(a[k//2]+a[(k//2)-1])/2)
            return float(s)
        else:
            s=a[k//2]
            return float(s)
        
