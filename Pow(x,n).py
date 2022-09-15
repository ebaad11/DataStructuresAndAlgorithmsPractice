class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        number, power = x,n
        
        if number == 0:
            return 0
        
        def pow(number,power):
            
            # BASE CASE i.e 100^0 = 1
            if power == 0:
                return 1
      
            #10 --> 5 --> 2 --> 1 --> 0 
            intermediate = pow(number,power//2)
            
            
            # 2 * 2 - 2^2 
            intermediate = intermediate * intermediate
            
            
            return intermediate if power %2 == 0 else number * intermediate
        
        
        result = pow(number,abs(power)) 
        return result if n>=0 else 1/result
