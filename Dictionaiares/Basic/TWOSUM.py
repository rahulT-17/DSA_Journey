# QUES : Classic Two-Sum problem 
arr = [2, 7, 11, 15]
target = 9

needed = 0
record = {}

for index,num in enumerate(arr) :
    needed = target - num 

    if needed in record :
        print([record[needed],index])
        break
    record[num] = index
