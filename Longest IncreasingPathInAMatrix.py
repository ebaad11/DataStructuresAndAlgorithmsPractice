class DFS:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        ROWS,COLS = len(matrix),len(matrix[0])
       
        def dfs(r,c,prev): 
            if min(r,c) < 0 or r == ROWS or c == COLS or prev <= matrix[r][c]: 
                # checking elements in the path not needed as all the elements in the previous path are going to be bigger numbers
                return 0
                
            # next layer DFS
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            
            ans = 0
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                ans = max(ans,dfs(nr,nc,matrix[r][c])+1)
                
            return ans
        
        
        
        LLP = 0
        for r in range(ROWS):
            for c in range(COLS):
                LLP = max(LLP,dfs(r,c,float("inf")))
                
        return LLP
      
      
 class Memo:
      def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        ROWS,COLS = len(matrix),len(matrix[0])
      
        memo = [[0]*(COLS+1) for i in range(ROWS+1)]
        
        def dfs(r,c,prev): 
            
            
            
            if min(r,c) < 0 or r == ROWS or c == COLS or prev <= matrix[r][c]: 
                # checking elements in the path not needed as all the elements in the previous path are going to be bigger numbers
                return 0
            
            if memo[r][c] != 0:
                return memo[r][c]
            
            
            
                
            # next layer DFS
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            
            ans = 1
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                ans = max(ans,dfs(nr,nc,matrix[r][c])+1)
            
            memo[r][c] = ans
            return ans
        
        
        
        LLP = 0
        for r in range(ROWS):
            for c in range(COLS):
                print(memo)
                LLP = max(LLP,dfs(r,c,float("inf")))
                
        return LLP
        
        
