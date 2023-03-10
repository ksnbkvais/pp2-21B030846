import re
s=str(input())
x='^[a-z]+_[a-z]+$' 

if re.search(x, s):  
    print("match")
else: print("no match")