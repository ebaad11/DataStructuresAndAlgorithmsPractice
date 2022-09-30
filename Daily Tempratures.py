class BruteForce:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result= [0]*len(temperatures)
        
        
        for start in range(len(temperatures)):
            daysTill = 1
            for cont in range(start+1,len(temperatures)):
                if temperatures[cont] > temperatures[start]:
                    result[start] = daysTill
                    break
                else:
                    daysTill+=1
                    

        return result 
      
      
class Optimized:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        
        stack = [] # [temprature,index]
        result = [0] * len(temperatures)
       
        
        for currentIndex in range(len(temperatures)):
            currentValue = temperatures[currentIndex]
            
            while stack and stack[-1][0] < currentValue:
                
                popedValue,popedIndex = stack.pop()
                daysAfter = currentIndex - popedIndex
                result[popedIndex] = daysAfter
                
            stack.append([currentValue,currentIndex])
    
        return result
      
     
