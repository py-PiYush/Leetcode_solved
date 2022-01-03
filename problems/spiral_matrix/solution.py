class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ''' 1 '''
        result = []
        if not matrix or not matrix[0]:
            return result
        compass = ((0, 1), (1, 0), (0, -1), (-1, 0))
        direction = 0
        steps = [len(matrix[0]), len(matrix) - 1]
        row, col = 0, -1
        while steps[direction%2]:
            for i in range(steps[direction%2]):
                row += compass[direction][0]
                col += compass[direction][1]
                result.append(matrix[row][col])
            steps[direction%2] -= 1
            direction = (direction + 1) % 4
        return result
        
        
        
        
        ''' 2 '''
        res=[]
        left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1
        direction=0
        
        while left<=right and top<=bottom:
            # traverse right
            if direction == 0:
                for i in range(left, right+1):
                    res.append(matrix[top][i])
                
                top+=1 # topmost row traversed
                
            #traverse down
            elif direction == 1:
                for i in range(top, bottom+1):
                    res.append(matrix[i][right])
                    
                right-=1 # rightmost column traversed
            
            
            #traverse left
            elif direction==2:
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                    
                bottom-=1 # bottommost row traversed
            
            
            #traverse upwards
            else:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                
                left+=1 # leftmost column traversed
            
            direction=(direction+1)%4
        return res
        
        
        
        
        '''???'''
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
        
        
        
        
        
        
        
        
        
        