class Memo:
    def change(self, amount: int, coins: List[int]) -> int:
        
        
        
        memo = [[-1 for j in range(amount+1)] for i in range(len(coins)+1)]
        
     
        def makeChange(idx,left):
            
            if memo[idx][left] != -1:
                return memo[idx][left]
            
            
            if left == 0:
                
                return 1
        
            ways = 0
            for i in range(idx,len(coins)):
                
                currentCoin = coins[i] 
                changePossible = left - currentCoin >= 0
                
                if changePossible:
                    ways += makeChange(i,left-currentCoin)
            
            
            memo[idx][left] = ways
            return memo[idx][left]
                    
                    
    
        return makeChange(0,amount)
    
    
    
    
            
