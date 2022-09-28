class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        q = deque() # always needs to be decreasing from left to right.
        result = []


        for index,value in enumerate(nums):

            while q and nums[q[-1]] <= value:
                # this means we don't need values before since we have a new max
                q.pop() # from right

            # might still need it
            q.append(index)
            
            startingIndexQ = q[0]
            # the elements in the q don't go over the elements in the window
            if index-startingIndexQ == k: 
                #[7,6,5] 4(to add) get rid of 7 as it is out of bounds
                q.popleft()
                
           
            # only add when the window is of appropriate size
            if index >= k-1:
                result.append(nums[q[0]])
                
        
        return result
      
      
      
    
    
            
            
            
    
            
