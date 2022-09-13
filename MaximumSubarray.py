class DivideAndConqure:
    def maxSubArray(self, nums: List[int]) -> int:
    
        return self.subArray(nums,0,len(nums)-1)
    
    
    def wholeSubArray(self,nums,l,r,m):
            
            maxLeft = float("-inf")
            maxRight = float("-inf")

            currentSum = 0
            for i in reversed(range(l,m+1)):
                currentSum += nums[i]
                maxLeft = max(maxLeft,currentSum)
            currentSum = 0  
            for j in range(m+1,r):
                currentSum += nums[j]
                maxRight = max(maxRight,currentSum)

            return maxRight + maxLeft

    
    def subArray(self,nums,l,r):

        if l == r:
            return nums[l]

        m = r + ((l-r)//2)


        L = self.subArray(nums,l,m)
        R = self.subArray(nums,m+1,r)
        C = self.wholeSubArray(nums,l,r,m)


        return max(L,R,C)
      
      
 class Kadane:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currentSum = 0
        maxSubarray = nums[0]
        for number in range(len(nums)):
            if currentSum < 0:
                currentSum = 0 
            currentSum+=nums[number]
            maxSubarray = max(maxSubarray,currentSum)
            
            
        return maxSubarray
      
      
 
