class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        
        
        if len(hand) % groupSize != 0:
            return False
        
        
        count = {}
    
        for c in hand:
            count[c] = 1 + count.get(c,0)
            
 
        cards = list(count.keys())
        heapq.heapify(cards) 
       
        
        while cards:
            starting = cards[0]
            
            for nextCard in range(starting,starting+groupSize):
                if nextCard not in count:
                    return False
                
                count[nextCard] -= 1
                
                if count[nextCard] == 0:
                    if nextCard != cards[0]:
                        return False
                    
                    heapq.heappop(cards)
            
            
        return True
