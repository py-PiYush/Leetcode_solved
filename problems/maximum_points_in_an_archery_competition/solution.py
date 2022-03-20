class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        maxScoreCache= Solution.createCache(12,numArrows); targets= 12
        
        remainingTargets= targets;arrowCount= numArrows
        Solution.calculateMaxScore(remainingTargets,arrowCount,aliceArrows,maxScoreCache)
        bobArrows= Solution.getBobArrows(maxScoreCache,aliceArrows,targets,numArrows)
        return bobArrows
    
    @staticmethod
    def calculateMaxScore(remainingTargets,arrowCount,aliceArrows,maxScoreCache):
        
        """
            The function calculates maxScore that Bob can earn
            using 'arrowCount' arrows and from 'remainingTargets' targets
        """
        
        if remainingTargets== 0 or arrowCount== 0:
            maxScore= 0; maxScoreCache[remainingTargets][arrowCount]= maxScore; return maxScore
        
        if maxScoreCache[remainingTargets][arrowCount]!= -1: return maxScoreCache[remainingTargets][arrowCount]
        
        targetIndex= remainingTargets-1
        # Can this target be hit optimally; If yes then lets check 
        # Which provides max score : hitting the target or leaving the target

        if arrowCount> aliceArrows[targetIndex]: 
            # Hitting may result in getting max Score

            # Hit
            currPointsHit= targetIndex
            currPointsHit+= Solution.calculateMaxScore(remainingTargets-1,arrowCount-(aliceArrows[targetIndex]+1),aliceArrows,maxScoreCache)

            #Not Hit
            currPointsNotHit= 0
            currPointsNotHit+= Solution.calculateMaxScore(remainingTargets-1,arrowCount,aliceArrows,maxScoreCache)

            currPoints= max(currPointsHit,currPointsNotHit)

        #  We may hit the target otherwise ,but the arrows will be wasted
		#  If the target can't be hit optimally. then lets not hit
        else:
            # We exclude hitting the target
            currPointsNotHit= 0
            currPointsNotHit+= Solution.calculateMaxScore(remainingTargets-1,arrowCount,aliceArrows,maxScoreCache)

            currPoints= currPointsNotHit

        maxScoreCache[remainingTargets][arrowCount]= currPoints
        return maxScoreCache[remainingTargets][arrowCount]

    @staticmethod
    def createCache(ROWS,COLS):
        cache= list()
        for _ in range(ROWS+1):cache.append([-1]*(COLS+1))
        return cache
                    
    @staticmethod
    def getBobArrows(cache,aliceArrows,targets,numArrows):
        remainingTargets= targets; arrowCount= numArrows
        
        bobArrows= [0]*targets
        while remainingTargets>0 and arrowCount>0:
            maxArrows= cache[remainingTargets][numArrows]
            targetIndex= remainingTargets-1
            
            if arrowCount> aliceArrows[targetIndex]:
                currPointsHit= targetIndex
                currPointsHit+= cache[remainingTargets-1][arrowCount-(aliceArrows[targetIndex]+1)]
                
                currPointsNotHit= 0
                currPointsNotHit+= cache[remainingTargets-1][arrowCount]
                
                if cache[remainingTargets][arrowCount]== currPointsHit:
                    
                    bobArrows[targetIndex]= (aliceArrows[targetIndex]+1) if remainingTargets!=1 else arrowCount
                    remainingTargets-= 1; arrowCount-= bobArrows[targetIndex]
                else: 
                    if remainingTargets== 1:bobArrows[targetIndex]= arrowCount
                    remainingTargets-= 1
                    
            else:
                if remainingTargets== 1:bobArrows[targetIndex]= arrowCount
                remainingTargets-= 1
                    
        return bobArrows
                