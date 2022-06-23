class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rowLen, colLen = len(matrix), len(matrix[0])
        heights = [0]*(colLen + 1)
        ans = 0
        for row in range(rowLen):
            for col in range(colLen):
                if matrix[row][col] == '1':
                    heights[col]+=1
                else:
                    heights[col] = 0
            ans = max(ans, self.largestRectangleArea(heights))
        return ans
                    
        
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h*w)
            stack.append(i)
        return ans
    