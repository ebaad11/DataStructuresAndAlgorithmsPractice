class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      
    

        left,right = 0,len(matrix[0])
        top,bottom = 0,len(matrix)
        result = []


        while left < right and top < bottom:
            
            for i in range(left,right):
                result.append(matrix[top][i])

            top+=1

            for i in range(top,bottom):
                result.append(matrix[i][right-1])

            right-=1
            
            if  not(left < right and top < bottom):
                break
                
            for i in reversed(range(left,right)):
         
                result.append(matrix[bottom-1][i])
            bottom-=1



            for i in reversed(range(top,bottom)):
                result.append(matrix[i][left])

            left+=1

        
        return result
        
        
        
