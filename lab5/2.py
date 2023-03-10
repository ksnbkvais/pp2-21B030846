import re
s=str(input())
x='ab{2,3}' 

if re.search(x, s):  
    print("match")
else: print("no match")