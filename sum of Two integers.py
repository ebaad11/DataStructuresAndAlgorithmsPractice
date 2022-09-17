class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        
        
              
        if a == 0:
            return b
        if b ==0:
            return a
        
        
        
        mask = 0xffffffff
        sum,carry = a,b
        while carry!=0:
            sum, carry = (sum ^ carry) & mask, ((sum & carry) << 1) & mask
        
        
        firstBitNegative =  (sum >> 31) & 1
        
        if firstBitNegative:
            return ~(sum ^ mask)
        else:
            return sum
        
        
        # in Python, every integer is associated with its two's complement and its sign.
        # However, doing bit operation "& mask" loses the track of sign. 
        # Therefore, after the while loop, a is the two's complement of the final result as a 32-bit unsigned integer.
        
    
