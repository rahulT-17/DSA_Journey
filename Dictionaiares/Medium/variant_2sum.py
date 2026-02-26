## QUES : Count Number of Pairs With Given Sum ?

arr = [1, 5, 7, 1]
target = 6 

freq = {}
count = 0 

for num in arr :
    needed = target - num 
    if needed in freq :
        count += freq[needed]     # CORE LOGIC :  this increment the frequency of needed number 
    
    if num in freq:
        freq[num] += 1 
    else :
        freq[num] = 1 
print(count)