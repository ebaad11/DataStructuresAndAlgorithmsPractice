class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        
        res =[]
        def generate(o,c,string):
            
            if o == n and c == n:
                res.append(string)
                return 
            
            openCapacity = o < n
            
            if openCapacity:
                string+="("
                generate(o+1,c,string)
                string = string[:-1]
                
            needClosing = c < o
            
            if needClosing:
                string+=")"
                generate(o,c+1,string)
                string = string[:-1]
                
                
        generate(0,0,"")
        return res
