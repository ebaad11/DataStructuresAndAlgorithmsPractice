# Contains Duplicate

## Question (in your own words)

---

We are given an integer array i.e [1,2,3,1], we have to find out if there is an integer that appears twice in the array. If there is such integer we return True, if not we return False.

## Inputs

---

### How will you do it by hand?

We will compare each element with every other element(not including itself), and if we see that element twice we return true, if not we return False.

Cases : 

True/Found/etc

```python
Case1 = [1,2,3,1]
We will compare 1 with(==) 2,3,1 we will find 1 coming twice, so this is true
```

False/not Found etc

```python
Case2 = [1,2,3,4]
We will compare 1 with(==) 2,3,4
We will compare 2 with(==) 3,4... etc 

We will not find any matching element so we return False

```

## Brute-force (If any)

---

### Explanation

We can do something as we did above, compare each element with every other element, except itself and if we find a match we can return True. If not we return False. How will we write the code to iterate over the array once with all integers, and compare each of those integers with every other integer in the array.

```python
Case1 = [1,2,3,1] 
for firstElementindex in range(len(nums)): #O(N)
	# this loop will give us 1,2,3,1
	# we can't compare the number we are looping over with itself.
	# so we start the comparison one index over firstElementindex + 1
	for secondElementIndex in range(firstElementindex+1,len(nums)): # O(N)
			
			# we have indexes we need to get the elements now
			firstElement = nums[firstElementindex] #O(1)
			secondElement = nums[secondElementIndex] #O(1)

				if firstElement == secondElement:
						return True

# if the true value is not returned the loops will exhaust themselves and we can
#return false outside the loops

return False

```

### Final Code

```python

#GIVES A TIME LIMIT EXCEDED ERROR, AS IT IS REALLY SLOW O(N^2)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #O(N)
        for firstElementindex in range(len(nums)):
            #O(N)
            for secondElementIndex in range (firstElementindex+1,len(nums)):
                
                #O(1+1)
                firstElement = nums[firstElementindex]
                secondElement = nums[secondElementIndex] 
                
                if firstElement == secondElement:
                    return True
                

        return False
```

### Time Complexity

> Time ⏰ O(N^2) Space 💾 O(1)
> 

## Optimized Solution

---

How can we optimize it, a run time better than O(N^2) is O(NlogN), usually we can get a LogN complexity when the array is **sorted**. Will sorting the array help in this case?

```python
Case1 = [1,1,2,3] 
# do you see a pattern here?
# The duplicates are right next to each other and we need to iterate the array
#only once O(N)

```

Sorting an array using python’s built in sort method takes NlogN time complexity.

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # O(NlogN)
        nums.sort() 
        #O(N)
        for index in range(1,len(nums)):
						#O(1+1)
            if nums[index-1] == nums[index]:
                return True
            
        return False
```

> Time ⏰ O(NLOGN) Space 💾 O(1)
> 

Can we do better?

Is there a way we can traverse the array once without sorting it first? What if we kept a record of what we kept seeing as we iterated over the array and return true if we have seen that element before. What data structure can we use that has constant look-up time. You guessed it it is a hash-table. Or a set or dictionary in python. We will have to store n elements at most in the worst case so the space complexity will be O(N).

```python
seen = set()

for number in nums: # iterating over elements now not indexes
	if number in seen:
			return True
  seen.add(number
```

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        #O(N) space
        seen = set()
        
        #O(N)
        for number in nums: # Fyi iterating over elements now, not indexes
	        
            #O(1) constant look up
            if number in seen:
                return True
            #O(1) constant insert
            seen.add(number)
        
        #no duplicate found
        return False
```

> Time ⏰ O(N) Space 💾 O(N)
> 

### Time Complexity of optimized Solution

Did we Save space?

No, we had to keep a record of what elements we saw

Did we Save time?

Yes, we brought it down from N^2 —> NlogN — > N

You can decide what solution is best for you when optimizing for either space or time.

### Bonus One liner

```python
def containsDuplicate(self, nums: List[int]) -> bool:
    return len(nums)!=len(set(nums))
```

## Links

---

### [PythonTutor(Visualized)](https://pythontutor.com/render.html#code=class%20Solution%3A%0A%20%20%20%20def%20containsDuplicate%28self,nums%29%3A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%23O%28N%29%20space%0A%20%20%20%20%20%20%20%20seen%20%3D%20set%28%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%23O%28N%29%0A%20%20%20%20%20%20%20%20for%20number%20in%20nums%3A%20%23%20iterating%20over%20elements%20now%20not%20indexes%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%23O%281%29%20constant%20look%20up%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20number%20in%20seen%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20%23O%281%29%20constant%20insert%0A%20%20%20%20%20%20%20%20%20%20%20%20seen.add%28number%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%23no%20duplicate%20found%0A%20%20%20%20%20%20%20%20return%20False%0A%20%20%20%20%20%20%20%20%0As%20%3D%20Solution%28%29%0As.containsDuplicate%28%5B1,2,3,1%5D%29%0As.containsDuplicate%28%5B1,2,3,4%5D%29&cumulative=false&curInstr=36&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

### Resources(if any)

---

None

### Leetcode Solution
