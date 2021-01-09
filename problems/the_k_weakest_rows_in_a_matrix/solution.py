class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        '''res=[]
        for i in range(len(mat)):
            res.append([i,sum(mat[i])])
        final= sorted(res,key=lambda x:x[1])
        return [i[0]for i in final][:k]'''
        scores = list(map(lambda l: sum(l), mat))
        scores_enum = list(enumerate(scores))
        print(scores_enum)
        
        ordered = sorted(scores_enum, key=lambda el: el[1])
        
        return [ordered[i][0] for i in range(k)]