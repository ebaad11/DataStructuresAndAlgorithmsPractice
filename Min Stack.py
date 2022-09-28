class MinStack:

    def __init__(self):
        
        self.stack = []
        self.minStack = [] # min value at each level of the stack
        

    def push(self, val: int) -> None:
        
        # update min
        if self.minStack:
            newMin = min(self.minStack[-1],val)
            self.minStack.append(newMin)
        else:
            self.minStack.append(val)
            
        self.stack.append(val)
        

    def pop(self) -> None:
        
        self.minStack.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        else:
            return "no min"
