# Given an array, find the second largest element : SORTING NOT ALLOWED

## CORE IDEA : track two value , while travesing over value in arr apply conditions
## 1. If num is bigger than max , the sec_max = old max while update the num = max 
## 2. for avoiding dupilcate we,ll apply one more condition where num is bigger than second num while != max sec_max = num 

arr = [1,3,4,5,7,6]

max_num = float('-inf')
second_max = float('-inf')

for num in arr :
    if num > max_num :
        second_max = max_num
        max_num = num 
    elif num > second_max and num != max_num :
        second_max = num 
print(second_max)


## Time: O(n) → one loop
## Space: O(1) → two variables
