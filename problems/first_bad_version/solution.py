# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # lo,hi=1,n
        # while lo<=hi:
        #     mid=(lo+hi)//2
        #     if isBadVersion(mid):
        #         if mid==1:
        #             return mid
        #         elif isBadVersion(mid-1):
        #             hi=mid-1
        #         else:
        #             return mid
        #     else:
        #         lo=mid+1
        
        l,r=1,n
        while l<r:
            mid=(l+r)//2
            if isBadVersion(mid):
                r=mid
            else:
                l=mid+1
        return l
            