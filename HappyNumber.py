class Solution:
    def isHappy(self, n: int) -> bool:
            
        seen = set()
   
        while True:
            
            
            s = 0
            for d in str(n):
                s += int(d)**2
            
            # return conditions
                # 1. if the sum == 1 : return True
                # 2. if sum is seen before we return False
            
            if s == 1:
                return True
            if s in seen:
                return False
            
            seen.add(s)
            
            # turning it back to integer
            n = s
            
  class Solution:
    def isHappy(self, n: int) -> bool:
            
        slow, fast = n, self.getNext(n) 
        
       
        while True:
            fast = self.getNext(self.getNext(fast))
            slow = self.getNext(slow)
            
            if slow == 1 or fast == 1:
                return True
            
            if slow == fast:
                return False
            
      
            
    def getNext(self, n):
        output = 0
        while n:
            print(n)
            output += (n % 10) ** 2
            n = n // 10
        return output
