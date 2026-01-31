# QUES : Given a string, find the first non-repeating character.
s = "aabbc1dde"
# Rule To Remeber : 1. to count non repeating character we'll always use 2 Loops 
# This helps in counting all the occuring freq of the char in "s".
# While 2 Loop helps in applying condition 
freq = {}
# 1st Loop
for ch in s :
    if ch in freq :
        freq[ch] += 1 
    else :
        freq[ch] = 1
# 2nd Loop
for ch in s :
        if freq[ch] == 1 :
          print(ch)
          break 
