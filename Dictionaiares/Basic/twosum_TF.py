# QUES : Just tell if any pair exists.
arr = [5, 3, 9 ,1] 
target = 10 

needed = 0

seen = {}

for i , num in enumerate(arr) :
    needed = target - num
    if needed in seen :
        print("True")
        break
    seen[num] = True
else :
    print("false")