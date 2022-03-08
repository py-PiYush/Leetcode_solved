class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        result=[[1]]
        
        for _ in range(1,numRows):
            temp1=result[-1]+[0]
            temp2=[0]+result[-1]
            result.append([temp1[i]+temp2[i] for i in range(len(temp1))])
        return result[:numRows]
            
        
        '''----------------------------'''
        res=[]
        for i in range(numRows):
            lst=[]
            for j in range(i+1):
                if j==0 or j==i:
                    lst.append(1)
                else:
                    lst.append(res[-1][j-1]+res[-1][j])
            res.append(lst[:])
        return res
        
        
            