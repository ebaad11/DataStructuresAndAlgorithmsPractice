
class Recursive:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        if n == 1:
            return True
        
        def jump(position):
            print(position)
            if position == len(nums)-1:
                return True
           
            
            for jumpLenght in range(nums[position]):
                
                #+1 as the range function includes zero,add zero to accomodate that
                if jump(position+jumpLenght+1):
                    return True
        
            
        return jump(0)


class Greedy:
    def canJump(self, nums: List[int]) -> bool:
        

        goal = len(nums)-1

        for i in range(len(nums)-1,-1,-1):
            goalReached = i+nums[i] >= goal
            if goalReached:
                goal= i

                
        return True if goal == 0 else False
        
