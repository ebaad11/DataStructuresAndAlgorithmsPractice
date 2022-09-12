
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def editDistance(i,j):
            
            #base Cases
            
            if i == len(word1) and j == len(word2):
                return 0
            
            
            if j == len(word2):
                return len(word1) - i
            
        
            if i == len(word1):
                return len(word2) - j
            
            
            
            #Skipping LCS
            if word1[i] == word2[j]:
                return editDistance(i+1,j+1)
            
            else:
            
                insert = editDistance(i,j+1)
                delete = editDistance(i+1,j)
                replace = editDistance(i+1,j+1)
                
                eachDecision = 1
                return eachDecision + min(insert,delete,replace)
            
            
        return editDistance(0,0)







class Memo:
    def minDistance(self, word1: str, word2: str) -> int:
    
        
        
        memo = [[-1] * (len(word2)+1) for i in range(len(word1)+1)]
        
    
        def editDistance(i,j):
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            #base Cases
            
            if i == len(word1) and j == len(word2):
                return 0
            
            
            if j == len(word2):
                return len(word1) - i
            
        
            if i == len(word1):
                return len(word2) - j
            
            
            
            #Skipping LCS
            if word1[i] == word2[j]:
                return editDistance(i+1,j+1)
            
            else:
            
                insert = editDistance(i,j+1)
                delete = editDistance(i+1,j)
                replace = editDistance(i+1,j+1)
                
                eachDecision = 1
                memo[i][j] = eachDecision + min(insert,delete,replace)
                
                return memo[i][j]
            
            
        return editDistance(0,0)
      
      
class DP:
    def minDistance(self, word1: str, word2: str) -> int:

        
        dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]
        
        
        #base cases 

            
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i
            
        
        
        
        
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                    
                else:
                   
                    
                    insert = dp[i][j+1]
                    delete = dp[i+1][j]
                    replace = dp[i+1][j+1]

                    eachDecision = 1
                    dp[i][j] = eachDecision + min(insert,delete,replace)

                    
        return dp[0][0]
                
        
