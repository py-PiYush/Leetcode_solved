class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        '''iterative'''
        MAPPING = ('0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')
        res = ['']
        for d in digits:
            res= [pre + cur for pre in res for cur in MAPPING[int(d)]]
        return res if len(digits) > 0 else []
        
        
        
        '''Backtracking'''
        
        let= 'abc,def,ghi,jkl,mno,pqrs,tuv,wxyz'.split(',')
        numToLet=dict(zip(range(2,10), let))
        ans=[]
        
        def dfs(i, res):
            if len(res)==len(digits):
                ans.append(res)
                return
            
            for c in numToLet[int(digits[i])]:
                dfs(i+1, res+c)
        
        if digits:
            dfs(0,'')
        return ans
                
                