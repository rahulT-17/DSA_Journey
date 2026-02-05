# QUES : Given an array, find the element with the maximum frequency . If multiple, return any one.
arr = [1, 2, 2, 3, 3, 3, 4]

freq = {}
# Again We have used 2 Loops to solve as we have told to find the element with max freq
# While we have to RETURN THE ELEMENT instead of its freq 
for num in arr :
    if num in freq :
       freq[num] += 1
    else :
        freq[num] = 1
print(freq)                 #This loop count the freq of each element 

# Here we have taken 2 variables 1.maxfreq 2.answer 
max_freq = 0          #counter variable 
answer = None         # To return the desired ekement 

for key in freq :                     # This loop checks for the keys in the freq 
    if freq[key] > max_freq:          # Compare the key with counter if greater add the key to counter 
        max_freq = freq[key]          
        answer = key                  # Lastly subsitute the key in answer
print(answer)

