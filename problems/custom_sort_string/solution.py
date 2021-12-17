class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        
        ans, cnt = [], collections.Counter(s)           
        for c in order:
            if cnt[c]: ans.extend(c * cnt.pop(c))      
        for c, v in cnt.items():
            ans.extend(c * v)                   
        return ''.join(ans);
    
    
    
    
#         res=''
#         cnt=Counter(s)
#         # print(cnt)
#         for i in order:
#             if i in cnt:
#                 res+=(i*cnt[i])
#                 cnt[i]=0
                
#         for i in cnt:
#             if cnt[i]:
#                 res+=(i*cnt[i])
            
        
#         return res