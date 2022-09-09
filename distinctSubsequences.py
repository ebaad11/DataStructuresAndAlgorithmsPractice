
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        
        #s = i index
        #t = j index
        
        # find t in s
        def distinctSubsequences(i,j):
            
            
            TNotFound = i == len(s) 
            #i goes over bound before j does
            TFound = j == len(t)
            
            if TFound:
                return 1
            if TNotFound:
                return 0
            
            
            if s[i] == t[j]:
            
                ways =  distinctSubsequences(i+1,j+1) + distinctSubsequences(i+1,j)
            else:
                ways = distinctSubsequences(i+1,j)
            
            return ways
        
        return distinctSubsequences(0,0)

class DP:
    def numDistinct(self, s: str, t: str) -> int:
        
        
        #s = i index
        #t = j index
        
        #find t in s
        
        
        memo = {}
        def distinctSubsequences(i,j):
            
            
            TNotFound = i == len(s) 
            #i goes over bound before j does
            TFound = j == len(t)
            
            if TFound:
                return 1
            if TNotFound:
                return 0
            
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            
            if s[i] == t[j]:
            
                ways =  distinctSubsequences(i+1,j+1) + distinctSubsequences(i+1,j)
            else:
                ways = distinctSubsequences(i+1,j)
            
            
            memo[(i,j)] = ways
            return ways
        
        return distinctSubsequences(0,0)
      
      
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        
        #s = i index
        #t = j index
        
        dp = {}
        
        # found
        for i in range(len(s) + 1):
            dp[(i, len(t))] = 1
        # not found
        for j in range(len(t)):
            dp[(len(s), j)] = 0
            
        for i in range(len(s)-1,-1,-1):
            for j in range(len(t)-1,-1,-1):
            
                if s[i] == t[j]:
                    dp[(i,j)] =  dp[(i+1,j+1)] + dp[(i+1,j)]
                else:
                    dp[(i,j)] = dp[(i+1,j)]

        
            
        
        return dp[(0,0)]
    
    
