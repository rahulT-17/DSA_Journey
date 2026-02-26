# QUES : Classic Two-Sum problem = 
'''
My understanding so far : what this problem states that in the given array find the any two num that makes up to a given target ,

Approach : 1. So the clear approach to solve this would be to use Hash Table , 
what this means is that while iterating over the arr we could easily store the numbers and their index together as key value pairs,
this would help in accessing the elements quickly as the avg Time-Complexity = O(1).

2. while we iterate over the arr we would start with setting our 'current' num as the first element in the arr (current = arr[1]). 

3. We would also check while iterating that 'needed' = 'target' - 'current'

4.  And IF we got the needed num in the Hash Table we could return the numbers or their.

Thinking : 1. Why are we doing "seen[current] = i and not seen[i] = current" is because :

reason = we are checking for the needed num is in the hash as a key , If we did other way around we would be saving the indices as the key
but we are checking for the key as needed num 

Core Principle : Hash tables are powerful if the thing we want to search is key not vice versa.


Twister : 2 ways for returning values in two-sum problem :
1 . return the values 
2. return the indices of them values

=> The key for this is that we change the return in if condition i.e we return if our needed num is in the hash table ,
return us the value where the num appear which would be the index , while with "i" which is the iterator.

=> return
 ''' 



def two_sum(arr,target) :
    seen = {}

    for i in range(len(arr)):
        current = arr[i]
        needed = target - current
 
        if needed in seen :                          # KEY : here we are checking if the needed num is in the hash (seen) as a key. 
            return (seen[needed],i) 
        
        seen[current] = i 
    
    return None

arr = [2, 7, 11, 15]
target = 9
print("the two num :" , two_sum(arr,target))


        