class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mapping = {} # cource : preReq
        for c in range(numCourses):
            mapping[c] = []
        for c, p in prerequisites:
            mapping[c].append(p)
           
        print(mapping)
            
        visited = set() # already visited
        cycle = set() # curently visiting
        order = []
        
        def dfs(cource):
            if cource in cycle:
                return False
            if cource in visited: # no need to visit again so return 
                return True
            
            # add to cycle
            cycle.add(cource)
            
            # else run on neighbours
            for n in mapping[cource]:
                # cycle found return False
                if not dfs(n):
                    return False
            
            # no cycle found]
            # cource Staus = visted 
            visited.add(cource)
            cycle.remove(cource)
            order.append(cource)
            return True
                

        
        for c in range(numCourses):
            if not dfs(c):
                return []
    
        return order
            
