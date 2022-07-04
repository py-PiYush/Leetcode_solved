class Solution:
    def candy(self, ratings: List[int]) -> int:
        ''' O(n) '''
        n=len(ratings)
        distribute = [1]*n
        for i in range(1, n):
            if ratings[i]>ratings[i-1]:
                distribute[i] = distribute[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i]>ratings[i+1]:
                distribute[i] = max(distribute[i], distribute[i+1] + 1)
        return sum(distribute)
        
        
        ''' Brute Force'''
        n=len(ratings)
        distribute = [1]*n
        hasChanged = True
        while hasChanged:
            hasChanged = False
            for i in range(n):
                if i>0 and ratings[i]>ratings[i-1] and distribute[i]<=distribute[i-1]:
                    distribute[i]=distribute[i-1]+1
                    hasChanged=True
                if i<n-1 and ratings[i]>ratings[i+1] and distribute[i]<=distribute[i+1]:
                    distribute[i] = distribute[i+1] + 1
                    hasChanged = True
            
        return sum(distribute)