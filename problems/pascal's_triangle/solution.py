class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[[1]]
        
        for _ in range(1,numRows):
            temp1=result[-1]+[0]
            temp2=[0]+result[-1]
            result.append([temp1[i]+temp2[i] for i in range(len(temp1))])
        return result[:numRows]
            
            