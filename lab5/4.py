import re
s=str(input())
x='[A-Z]+[a-z]+$' 

if re.search(x, s):  
    print("match")
else: print("no match")

