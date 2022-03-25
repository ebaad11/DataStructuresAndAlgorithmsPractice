def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        
        #left and right pointer denoting the size of the window
        #initial size of the window is 0
        
        left=0
        right=0
        
        
        # will represent all the unique items in the sliding window
        uniqueCharacters = set()
        maxLenghtSubstring = len(set())
        
        #will keep moving the right pointer 
        #until we reached end of the string    
        while (right < len(s)):
           
        #First Condition
            # if the character is not in the set, 
            #this means it is a unique element 
            #between the two pointer
            if (s[right] not in uniqueCharacters):
                #we add it to the uniqueCharaters set
                uniqueCharacters.add(s[right])
                
                #move the right pointer
                right +=1
                
                #in the next Iteration
                #will see if character after is unique
                
                
                #Setting the max lenght to the size of teh set
                #update when a new threshold for size is reached
                maxLenghtSubstring = max(maxLenghtSubstring, len(uniqueCharacters))
                
        #Second Condition
            #when the character is already in the set 
            #we remove the left most chacter that is in the set
            #and we move the left pointer
            #we keep doing this with iterations until we reach 
            #a state where there are only unique items in the uniqueCharacters set
            
            else:
                uniqueCharacters.remove(s[left])
                left+=1
        
        # we return the maxLenghtSubstring
        return maxLenghtSubstring


print(lengthOfLongestSubstring("abcabcbb"))
# print(lengthOfLongestSubstring("pwwkew"))
# print(lengthOfLongestSubstring("bbbbb"))