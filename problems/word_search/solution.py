class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        path=set()
        
        def helper(row, col, idx):
            if idx==len(word):
                return True
            if (row<0 or col<0 or 
                row>=ROWS or col>=COLS or 
                word[idx]!=board[row][col] or (row, col) in path):
                return False
            path.add((row, col))
            res= (helper(row-1, col, idx+1) or 
                  helper(row+1, col, idx+1) or 
                  helper(row, col-1, idx+1) or 
                  helper(row, col+1, idx+1))
            path.remove((row, col))
            return res
                
        for r in range(ROWS):
            for c in range(COLS):
                if helper(r,c,0):
                    return True
        return False