class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def helper(idx, target, res):
            if target==0:
                ans.append(res[:])
                return
            for i in range(idx, len(candidates)):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                if target<candidates[i]:
                    break
                helper(i+1, target-candidates[i], res+[candidates[i]])
        
        candidates.sort()
        ans=[]
        helper(0,target, [])
        return ans