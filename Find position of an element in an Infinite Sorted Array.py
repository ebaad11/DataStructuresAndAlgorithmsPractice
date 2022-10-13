def findBounds(array,target):
    
    l,r = 0,1
    
    while array[r] < target:
        l = r
        r = 2 * r
        
    return l,r



def binarySearch(l,r,array,target):
    
    
    while l <= r:
        mid = l + (r-l)//2
        
        
        if array[mid] == target:
            return mid
        
        if array[mid] > target:
            r = mid - 1
            
        else:
            l = mid + 1
            
array= [1,2,3,5,7,8,9,10,13,14,15]           
   
l,r = findBounds(array,9)
binarySearch(l,r,array,9)
