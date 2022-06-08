class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ''' 1 '''
        A, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [range(lo, hi)] + list(zip(*A[::-1]))
        return A
        
        
        
        ''' tweaks in spiral matrix'''
        res = [[0]*n for _ in range(n)]
        left, right, top, bottom = 0, n-1, 0, n-1
        fill = 0
        direction = 0
        
        while left<=right and top<=bottom:
            if direction == 0:
                for i in range(left, right+1):
                    fill+=1
                    res[top][i]=fill
                top+=1
                    
            elif direction == 1:
                for i in range(top, bottom+1):
                    fill+=1
                    res[i][right] = fill
                right-=1
                
            elif direction == 2:
                for i in range(right, left-1, -1):
                    fill+=1
                    res[bottom][i]=fill
                bottom-=1
            
            else:
                for i in range(bottom, top-1, -1):
                    fill+=1
                    res[i][left]=fill
                left+=1
            
            direction=(direction+1)%4
            
        return res
        
        
        
        '''----------------------------'''
        res=[[0 for _ in range(n)] for _ in range(n)]
        compass = [(0,1), (1,0), (0,-1), (-1, 0)]
        direction=0
        row, col=0,-1
        count=0
        steps=[n, n-1]
        while steps[direction%2]:
            for i in range(steps[direction%2]):
                count+=1
                row+=compass[direction][0]
                col+=compass[direction][1]
                res[row][col]=count
            
            steps[direction%2]-=1
            direction=(direction+1)%4
        return res
            