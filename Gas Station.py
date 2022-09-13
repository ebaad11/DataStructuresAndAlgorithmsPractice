class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        total = 0
        for i in range(len(gas)):
            
            total += gas[i] - cost[i]
            
            ranOutOFGas = total < 0
                
            if ranOutOFGas:
                total = 0
                start = i+1
                
        return start
