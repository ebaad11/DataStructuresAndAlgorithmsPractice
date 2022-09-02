class Recursive:
    def rob(self, nums: List[int]) -> int:
        
        left = len(nums)
        
        if left == 0:
            return 0 
        elif left == 1:
            return nums[0]
        elif left == 2:
            return max(nums[0], nums[1])
        else:
            return max(nums[0] + self.rob(nums[2:]),self.rob(nums[1:]))


class Memo:
    def rob(self, nums: List[int]) -> int:
        memo = [None] * (len(nums)+1)
        
        def dfs(nums):
            left = len(nums)
            if memo[left]:
                return memo[left]

            if left == 0:
                return 0 
            elif left == 1:
                return nums[0]
            elif left == 2:
                return max(nums[0], nums[1])
            else:
                memo[left] = max(nums[0] + dfs(nums[2:]),dfs(nums[1:]))
                return memo[left]
        return dfs(nums)




class DP:

    def rob(self, nums: List[int]) -> int:
      
        if len(nums) <= 1:
            return nums[0]
        
        dp = [None] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        
        
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
            
                
        return dp[-1]
        
        
        
class FurtherOptimization:

    def rob(self, nums: List[int]) -> int:
      
        if len(nums) <= 1:
            return nums[0]
        

        rob1 = nums[0]
        rob2 = max(rob1,nums[1])
        
        
        for i in range(2,len(nums)):
            toRob = max(nums[i]+rob1,rob2)
            rob1 = rob2 
            rob2 = toRob
            
            
                
        return rob2
