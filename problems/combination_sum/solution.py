class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def helper(idx, target, res):
            if idx==len(candidates) and target==0:
                ans.append(res[:])
                return 
            if idx==len(candidates):
                return
            elem=candidates[idx]
            if elem<=target:
                helper(idx, target-elem, res+[elem])
            helper(idx+1, target, res)
        
        ans=[]
        helper(0,target, [])
        return ans