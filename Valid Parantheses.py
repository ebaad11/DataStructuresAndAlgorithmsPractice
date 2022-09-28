class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack = []
        
        opening = set(brackets.values())
        closing = set(brackets.keys())
        
        
        
        for parentheses in s:
            
            if parentheses in closing:
                
                if len(stack) == 0:
                    return False
                
                else:
                    if brackets[parentheses] != stack.pop():
                        return False
                    
            
            # opening
            else: 
                stack.append(parentheses)
          
        
        
        return True if (len(stack) == 0) else False
                
