class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''stack and dictionary'''
        stack, mapp = [], {}
        for n in nums2:
            while stack and stack[-1]<n:
                mapp[stack.pop()]=n
            stack.append(n)
        
        return [mapp.get(x, -1) for x in nums1]
        
        
        
        '''-----brute force----'''
        res=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    temp=nums2[j]
                    for k in range(j, len(nums2)):
                        if nums2[k]>temp:
                            res.append(nums2[k])
                            break
                        if k==len(nums2)-1:
                            res.append(-1)
        return res