class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        #TLE
        '''max=0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                x=j-i
                y=min(height[j],height[i])
                area=x*y
                if area>max:
                    max=area
        return max'''
        
        s=0
        e=len(height)-1
        max_=0
        while s<e:
            x=e-s
            y=min(height[e],height[s])
            area=x*y
            if area>max_:
                max_=area
            if y==height[e]:
                e-=1
            else:
                s+=1
        return max_
        