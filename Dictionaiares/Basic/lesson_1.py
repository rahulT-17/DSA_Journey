# QUES : Given an array of numbers, find the frequency of each number ?
arr = [10, 2, 5, 10, 1, 2]

# solving using dictonaires : to count the freq of each number 
freq ={}
# FOR looping over the arr to count the repeating no.s
for num in arr :
    if num in freq :         #using condition that if nums are in freq then increment the Value of that Key
        freq[num] += 1
    else :
        freq[num] = 1
print(freq)