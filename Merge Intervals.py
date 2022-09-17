class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda val:val[0])
        result = []
        
        result.append(intervals[0])
        
        
        
        for iterating in range(1,len(intervals)):
            
            prevStart = result[-1][0]
            prevEnd = result[-1][1]
            
            interatingIntervalStart = intervals[iterating][0]
            interatingIntervalEnd = intervals[iterating][1]
        
            overlap = prevEnd >=  interatingIntervalStart
            
            if overlap:
                result[-1][0] = min(prevStart,interatingIntervalStart)
                result[-1][1] = max(prevEnd,interatingIntervalEnd) 
                
            else:
                result.append(intervals[iterating])
                
                
        return result
        
        
