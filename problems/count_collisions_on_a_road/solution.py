class Solution:
    def countCollisions(self, directions: str) -> int:
        '''----One-liner----'''
        return sum(dir!='S' for dir in directions.lstrip('L').rstrip('R'))
        
        
        
        '''-------Contest------'''
	    #col: An integer to store number of collisions
        col=0
        col+=2*directions.count('RL')
        directions = directions.replace('RL', 'S')
		
		#r, l: denotes the numbers of 'R' and 'L' b/w 'S'
		#s: checks if there exist 'S' to the left of our current index
        r, l, s = 0,0,0
        for i in range(len(directions)):
            if directions[i]=='R':
                r+=1
            if directions[i]=='L':
                l+=1
				
			#when we encounter a 'S', all the r 'R' will collide to this 'S'
            if directions[i]=='S':
                col+=r
			    #if there exists a 'S' to the left of current index, all the l 'L' will collide to that 'S'
                if s:
                    col+=l
            
                s=1
                l, r = 0,0
        if s:
            col+=l
        
        return col