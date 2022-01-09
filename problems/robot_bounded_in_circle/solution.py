class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        '''
            Starting at the origin and face north (0,1),
    after one sequence of instructions,

        if chopper return to the origin, he is obvious in an circle.
        if chopper finishes with face not towards north,
        it will get back to the initial status in another one or three sequences.
        '''
        dirX, dirY = 0,1
        x,y=0,0
        for ins in instructions:
            if ins=='G':
                x,y=x+dirX, y+dirY
            elif ins=='R':
                dirX, dirY = dirY, -dirX
            else:
                dirX, dirY = -dirY, dirX
        
        return (x,y) == (0,0) or (dirX, dirY) != (0,1)