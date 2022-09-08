class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        
        def ways(i,total):
            
            if total == target and i >= len(nums):
                return 1
        
            if i >= len(nums):
                return 0
        
            positive = ways(i+1,total+nums[i])
            negative = ways(i+1,total-nums[i])
            
            return positive + negative
        
        
        return ways(0,0)
    
    
class memo:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        memo = {}
        
        
        def ways(i,total):
      
            if (i,total) in memo:
                return memo[(i,total)]
            
            if total == target and i >= len(nums):
                return 1
        
            if i >= len(nums):
                return 0
        
            positive = ways(i+1,total+nums[i])
            negative = ways(i+1,total-nums[i])
            
            
            memo[(i,total)] = positive + negative
            return memo[(i,total)]
        
    
        return ways(0,0)
 


 class memoArray:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        memo = [[-1 for j in range(10000)] for i in range(len(nums)+1)]
        
        
        def ways(i,total):
            
            if memo[i][total] != -1:
                return memo[i][total]
            
            if total == target and i >= len(nums):
                return 1
        
            if i >= len(nums):
                return 0
        
            positive = ways(i+1,total+nums[i])
            negative = ways(i+1,total-nums[i])
            
            
            memo[i][total] = positive + negative
            return memo[i][total]
        
        
        return ways(0,0)
    
    
    
