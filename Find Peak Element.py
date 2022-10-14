class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        
        
        l,r = 0,len(nums)-1
        while l <= r:
            
            
            m = l + (r-l)//2
            inBounds = m > 0 and m < len(nums)-1
           
            
            if inBounds:
                
                peak = nums[m-1] < nums[m] and nums[m] > nums[m+1]
                
                peakToTheRight = nums[m] < nums[m+1]
                peakToTheLeft =  nums[m] < nums[m-1]
                
                if peak:
                    return m
                
                elif peakToTheRight:
                    l = m + 1
                    
                elif peakToTheLeft:
                    r = m - 1
                  
            #corner elements
            else:
                if m == 0:
                    if nums[m] > nums[m+1]: # m[0] > m[1]
                        return m # 0
                    else:
                        return m+1 # 1
                    
                elif m == len(nums)-1:
                    if nums[m] > nums[m-1]:
                        return m
                    
                    else:
                        return m-1
