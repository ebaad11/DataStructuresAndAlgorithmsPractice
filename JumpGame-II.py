class Recursive:

    def jump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        if n == 1:
            return  0
        
        def jump(position):
            if position == len(nums)-1:
                return 0
            
            if position > len(nums)-1:
                return 0
        
            minJumps = float("inf")
            for jumpLenght in range(nums[position]):
                
                #+1 as the range function includes zero,add zero to accomodate that
                minJumps = min(minJumps,jump(position+jumpLenght+1))
                   
            return minJumps +1
        
            
        return jump(0)
      
      
class Greedy:

    def jump(self, nums: List[int]) -> bool:
        
        destination = len(nums)-1
        
        l,r = 0,0
        res = 0
        farthest = 0
        
        while r < destination:
            
            # 1 jump
            for i in range(l,r+1):
                
                _from = i
                to = nums[i]
                jumpLenght = _from + to
                
                farthest = max(farthest,jumpLenght)
            
            l = r+1    
            r = farthest 
            
            res+=1
            
        return res
            
            
