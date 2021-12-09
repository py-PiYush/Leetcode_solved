class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # new=s[::-1]
        # for i in range(len(s)):
        #     s[i]=new[i]
        
        '''Iterative'''
        # start,end=0,len(s)-1
        # while start < end:
        #     s[start],s[end]=s[end],s[start]
        #     start+=1
        #     end-=1
        
        
        for i in range(len(s)//2):
            s[i],s[~i]=s[~i],s[i]
        '''Recursive'''
        
        # l=len(s)
        # if l<2:
        #     return s
        # return self.reverseString(s[l//2:])+self.reverseString(s[:l//2])
    
#         def recurse(s, start, end):
#             if start>=end:
#                 return
#             s[start], s[end]=s[end], s[start]
#             recurse(s, start+1, end-1)
            
#         start, end=0, len(s)-1
#         recurse(s, start, end)