class BruteForce:
    def minWindow(self, s: str, t: str) -> str:
        
        countT = {}
        for char in t:
            countT[char] = 1 + countT.get(char,0)
            
        matchesNeed = len(countT) # regradless of duplicates
        output = ""
        minLenghtOutput = float("inf")
        
        
        for left in range(len(s)):
            # Reset
            countS = {}
            matchesHave = 0
            
            for right in range(left,len(s)):
                
                charAdded = s[right]
                lenghtOfWindow = right-left+1
                
                # Extend Right to add Char from S
                #__________________________________________________________________
                countS[charAdded] = 1 + countS.get(charAdded,0)
                
                
                # CRITERIA
                # If the same characters with the same frequency exist in both Hashmaps
                #__________________________________________________________________
                if charAdded in countT and countS[charAdded] == countT[charAdded]:
                    matchesHave +=1

                if matchesNeed == matchesHave:
                    
                    if lenghtOfWindow < minLenghtOutput:
                        minLenghtOutput = lenghtOfWindow
                        output = s[left:right+1]
                        break
    
        
        return output
      
      
 class TwoPointer:
    def minWindow(self, s: str, t: str) -> str:
        
        countT = {}
        for char in t:
            countT[char] = 1 + countT.get(char,0)
            
        matchesNeed = len(countT) # regradless of duplicates
        output = ""
        minLenghtOutput = float("inf")
        
        
       
        left = 0
        # Reset
        countS = {}
        matchesHave = 0

        for right in range(left,len(s)):

            charAdded = s[right]

            # Extend Right to add Char from S
            #__________________________________________________________________
            countS[charAdded] = 1 + countS.get(charAdded,0)


            # CRITERIA
            # If the same characters with the same frequency exist in both Hashmaps
            #__________________________________________________________________
            if charAdded in countT and countS[charAdded] == countT[charAdded]:
                matchesHave +=1

            while matchesNeed == matchesHave:
                lenghtOfWindow = right-left+1
            
                if lenghtOfWindow < minLenghtOutput:
                    minLenghtOutput = lenghtOfWindow
                    output = s[left:right+1]
                    
                    
                # Remove from left and delete Char from S
                #__________________________________________________________________
                charRemove = s[left]
                countS[charRemove] -=1
                
                if charRemove in countT and countS[charRemove] < countT[charRemove]:
                    matchesHave -=1 
                    
                left+=1

        
        return output
    
    
