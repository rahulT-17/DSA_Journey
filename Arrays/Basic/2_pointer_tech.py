# here try to understand the 2 pointer technique and how it works :

""" the 2 pointer technique is a powerful technique that can be used to
     solve many problems in arrays and linked lists.

     It is a technique that uses 'two pointers' to 'traverse the array' or 
     linked list and solve the problem in O(n) time complexity. """

# QUES : Given an array of integers, find the two numbers that add up to a specific target ?


# we can solve this problem using the 2 pointer technique 
# by sorting the array and then using two pointers to find the two numbers that add up to the target 

""" Time Complexity : O(n log n) because we need to sort the array first and then we need to traverse the array using two pointers which takes O(n) time complexity.
 Space Complexity : O(1) because we are not using any extra space to solve this problem."""



def has_pair_with_sum(arr, target) :
    
    #Assigning the left and right pointers"
    left = arr[0]
    right = len(arr) - 1  #this is because in python, the index starts from 0 and the last index is len(arr) - 1"
  
     
    while left < right : #this is because we need to check the elements at the left and right pointers until they meet each other

    
        current_sum = arr[left] + arr[right] #this is the current sum of the elements at the left and right pointers

        if current_sum == target : #if the current sum is equal to the target, then we have found the two numbers that add up to the target
           return True 
        elif current_sum < target : #if the current sum is less than the target, then we need to move the left pointer to the right to increase the sum
            left += 1 
        else : #if the current sum is greater than the target, then we need to move the right pointer to the left to decrease the sum
            right -= 1 
    
    return False #if we have traversed the entire array and we have not found any pair of numbers that add up to the target, then we return False
  
arr = [1, 2, 3, 4, 6]
target = 6

print(has_pair_with_sum(arr,target))