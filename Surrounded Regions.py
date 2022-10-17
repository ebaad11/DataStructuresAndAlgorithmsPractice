class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS,COLS = len(board),len(board[0])
        path = set()
        # do we need path?
        def surrounded(r,c,path):
            
            # not a valid surround
            
            if r < 0 or c < 0 or r == ROWS or c == COLS:
                return False
            
            if board[r][c] == "X" or (r,c) in path:
                return True
            
            if board[r][c] == "O":
                # captured if surrounded by foursides
                path.add((r,c))
                captured = (
                surrounded(r-1,c,path) and
                surrounded(r+1,c,path ) and
                surrounded(r,c-1,path) and
                surrounded(r,c+1,path )
                )
                path.remove((r,c)) # ?
                
                if captured:
                    # make enemy Teritory 
                    board[r][c] = "X"
                    
                return captured
            
            
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    surrounded(r,c,path)
                    
        return board
                    
