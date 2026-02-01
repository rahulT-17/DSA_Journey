# QUES : Return the numbers, not indices.

arr = [1, 4, 6, 8]
target = 10
# ANS : (4, 6)

needed = 0 
want = {}

for i , num in enumerate(arr) :     # here we are telling the for loop that go through each index and its corresponding elemt in arr 
    needed = target - num           # this line gets us the needed value asked in the ques

    if needed in want :             # codition : if needed num appears in the dict print the needed and the num we that got us the needed num 
        print(needed,num) 
        break                       # After getting the num print the values and break thee loop
    want[num] = i                   # this line save the num at its index

    # here the i , num represent that ,
    # im standing at this index looking at the num in the arr