class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        """
        # nums1[m:] = nums2[:n]
        # nums1.sort()
        
        temp=nums1[:m]
        p1,p2,final=0,0,0
        while p1<len(temp) and  p2<len(nums2):
            if temp[p1]<=nums2[p2]:
                nums1[final]=temp[p1]
                p1+=1
                final+=1
            elif temp[p1]>nums2[p2]:
                nums1[final]=nums2[p2]
                p2+=1
                final+=1
        if p1<len(temp):
            nums1[final:]=temp[p1:]
        elif p2<len(nums2):
            nums1[final:]=nums2[p2:]