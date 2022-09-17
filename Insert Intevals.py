class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        
        result = []
        

        for i in range(len(intervals)):
        
            newStarting = newInterval[0]
            newEnding = newInterval[1]
            starting= intervals[i][0]
            ending= intervals[i][1]

            beforeTheIteratingInterval = starting > newEnding
            afterTheIteratingInterval = newStarting > ending
            
            
            if beforeTheIteratingInterval:
                result.append(newInterval)
                result.extend(intervals[i:])
                
                return result
            
            elif afterTheIteratingInterval:
                result.append(intervals[i])
            
            
            #overlap
            else:
                newInterval[0] = min(newStarting,starting)
                newInterval[1] = max(newEnding,ending)
                
        result.append(newInterval)
        return result
