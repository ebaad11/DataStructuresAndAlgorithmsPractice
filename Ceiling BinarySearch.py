array = [1,2,4,4,5,5,8,10,10,12,19]


def ceil(array,key):
    
    l,r= 0,len(array)-1
    res = None
    while l <= r:
        mid = l + (r-l)//2
        
        if array[mid] == key:
            return mid
        
        
        if array[mid] < key:
            l = mid + 1
        else:
            res = mid
            r = mid-1
            
           
            
            
print(ceil(array,9))

