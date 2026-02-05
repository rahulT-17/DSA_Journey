# FINDING THE MAX VALUE IN AN ARRAY :
## CORE CONCEPT OF THIS IS THAT WE HAVE TO ASSSUME THE MAX_VAL IS AT THE INDEX 0
arr = [10,20,70,30,50]

max_value = arr[0] 

for i in range(1, len(arr)) :
    if arr[i] > max_value :
       max_value = arr[i]
print(max_value)