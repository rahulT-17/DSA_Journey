"Lesson on Time Complexity and Space Complexity of Arrays"

# WHAT IS AN ARRAY : ARRAYS ARE A CONTINOUS BLOCK OF MEMORTY WHICH STORES SIMILAR DATA TYPE ELEMENTS :

''' this is why the Big O Notation of accessing an element in an array is O(1)
       because we can directly access the element using its index. arr[index] = O(1) 
       ''' 
 
# CREATING AN ARRAY IN PYTHON :
# we can create an array using the list data structure in python. we can also use the array module to create an array but it is not commonly used in python.

arr = [1, 2, 3, 4, 5] # this is an array of integers
print(arr) # [1, 2, 3, 4, 5]

"""The Time Complexity of accessing an element in an array is O(1) because ,
 we can directly access the element using its index ,
 arr[index] = O(1)"""

"""The Space Complexity of an array is O(n) because we need to allocate space for n elements in the array"""

# Here we gonna see some basic operations on arrays and their Time Complexity and Space Complexity :

# 1. Appending an element in an array :

"Big O Notation : appending an element in an array is O(1) because we can directly add the element at the end of the array. arr.append(element) = O(1)"
"""Time Complexity : O(1)
Space Complexity : O(1) :

This is because we can directly access the element using its index and we are not using any extra space to access the element."""

# 2. Inserting an element in an array at the beigning or in the middle of the array :
"Big O Notation : inserting an element in an array at the beginning or in the middle is O(n) because we need to shift all the elements to the right of the index where we want to insert the element. arr.insert(index, element) = O(n)"
"""Time Complexity : O(n)
Space Complexity : O(1) 

This is because we need to shift all the elements to the right of the index where we want to insert the element and we are not using any extra space to insert the element."""
