class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg = 0
        for row in range(len(grid)):
            current_row = grid[row]
            l, r = 0, len(grid[0])
            while l < r:
                mid = (l + r) // 2
                if current_row[mid] < 0:
                    r = mid
                else:
                    l = mid+1
            neg += (len(current_row) - l)
        return neg
    
        