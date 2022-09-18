class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        
        
        minHeap = []
        
        res = {}
        
        #[2,19,5,22]
        for q in sorted(queries):
            i = 0 
            
            #minHeap = [(lenght of query, right bound)]
            while i < len(intervals) and intervals[i][0] <= q:
                l,r = intervals[i]
                heapq.heappush(minHeap,((r-l+1),r))
                i+=1
            
            # get rid of all the invalid queries
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
                
                
            res[q] = minHeap[0][0] if minHeap else -1
        
            
        return [res[q] for q in queries]
    
    
    
