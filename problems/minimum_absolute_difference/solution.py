class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        '''Counting sort'''
        line=[0]*(max(arr)-min(arr)+1)
        shift=-min(arr)
        res=[]
        for i in range(len(arr)):
            line[shift+arr[i]]+=1
        
        mindiff=max(arr)-min(arr)
        prev=0
        for cur in range(1, max(arr)+shift+1):
            if line[cur]:
                if cur-prev<mindiff:
                    res=[]
                    mindiff=cur-prev
                if cur-prev==mindiff:
                    res.append([prev-shift, cur-shift])
                prev=cur
        return res
        
        '''Sorting'''
        # diff=0
        # mindiff=float('inf')
        # res=[]
        # arr.sort()
        # for i in range(len(arr)-1):
        #     diff=arr[i+1]-arr[i]
        #     if diff<mindiff:
        #         res=[]
        #         mindiff=diff
        #     if diff==mindiff:
        #         res.append([arr[i], arr[i+1]])
        # return res
    
    
    
        '''Brute Force (TLE)'''
#         res=[]
#         diff=0
#         mindiff=float('inf')
#         for i in range(len(arr)-1):
#             for j in range(i+1,len(arr)):
#                 diff=abs(arr[i]-arr[j])
#                 if diff < mindiff:
#                     res=[]
#                     mindiff=diff
                    
#                 if diff==mindiff:
#                     res.append([min(arr[i], arr[j]), max(arr[i], arr[j])])
#         return sorted(res)