class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def helper(num, target, k, res):
            if len(res)==k and target==0:
                ans.append(res[:])
                return 
            
            if len(res)>k:
                return
            
            for i in range(num, 10):
                if target<i:
                    break
                helper(i+1, target-i, k, res+[i])
        
        ans=[]
        helper(1, n, k, [])
        return ans