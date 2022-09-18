class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.pointsList = []
        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        
        # we need duplicates
        self.pointsList.append(point)
        

    def count(self, point: List[int]) -> int:
        
        
        count = 0
        qx,qy = point
        for x,y in  self.pointsList:
            
            p1 = (x,qy) 
            p2 = (qx,y)
            
            overlapingDiagonal = x == qx or y == qy
            
            
            if overlapingDiagonal:
                continue
            
            sameWidthAndHeight =  (abs(qy - y) == abs(qx - x))
            square = p1 in self.points and p2 in self.points and sameWidthAndHeight
            
            if square:
                count += self.points[p1] * self.points[p2]
                
                
        return count
                
